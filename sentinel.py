import os
import json
import time
from datetime import datetime
import geolocator      # Import our scout
import risk_analyzer   # Import our brain

# Configuration
LOG_FILE = "/var/log/auth.log"
JSON_LOG = "security_events.json"
BLOCK_LIST_FILE = "blocked_ips.txt"

def block_ip(ip):
    # Ensure block list exists
    if not os.path.exists(BLOCK_LIST_FILE):
        open(BLOCK_LIST_FILE, "w").close()

    with open(BLOCK_LIST_FILE, "r") as f:
        if ip in f.read():
            return False

    os.system(f"sudo ufw deny from {ip}")
    with open(BLOCK_LIST_FILE, "a") as f:
        f.write(f"{ip}\n")
    return True

def monitor():
    print(f"[+] {datetime.now()} - Shield Active & Monitoring Logs...")
    
    # Track failed attempts in memory for this session
    stats = {}

    with open(LOG_FILE, "r") as f:
        # Jump to the end of the file so old logs aren't processed
        f.seek(0, os.SEEK_END)

        while True:
            line = f.readline()
            if not line:
                time.sleep(1) # Wait for new logs
                continue

            if "Failed password" in line:
                # Extract IP (Usually 4th from the end in auth.log)
                parts = line.split()
                ip = parts[-4]
                
                stats[ip] = stats.get(ip, 0) + 1
                
                # Get Intelligence
                geo_data = geolocator.get_geo_info(ip)
                risk_level, score = risk_analyzer.calculate_risk(ip, stats[ip], geo_data)

                if risk_level == "High":
                    blocked = block_ip(ip)
                    
                    event = {
                        "timestamp": str(datetime.now()),
                        "ip": ip,
                        "risk_score": score,
                        "country": geo_data['country'],
                        "isp": geo_data['isp'],
                        "action": "BLOCKED" if blocked else "ALREADY_BANNED"
                    }

                    with open(JSON_LOG, "a") as log_out:
                        log_out.write(json.dumps(event) + "\n")

                    if blocked:
                        print(f"[!] {risk_level} RISK: Blocked {ip} ({geo_data['country']}) - Score: {score}")

if __name__ == "__main__":
    try:
        monitor()
    except KeyboardInterrupt:
        print("\n[+] Sentinel shutting down safely.")



