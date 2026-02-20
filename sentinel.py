import os 
import requests
import json
import time
from datetime import datetime

#Configuration
LOG_FILE = "/var/log/auth.log"
BLOCK_LIST_FILE = "blocked_ips.txt"
JSON_LOG = "security_events.json"
THRESHOLD = 1

#GEO-LOCATION
def get_geo_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if response['status'] == 'success':
            return response['country']
    except:
        pass
    return "Unknown"

#Mitigation
def block_ip(ip):
    if not os.path.exists(BLOCK_LIST_FILE):
        open(BLOCK_LIST_FILE, "w").close()

    with open(BLOCK_LIST_FILE, "r") as f:
        if ip in f.read():
            return False

    os.system(f"sudo ufw deny from {ip}")

    with open(BLOCK_LIST_FILE, "a") as f:
        f.write(f"{ip}\n")
    return True

def run_sentinel():
    print (f"[+] {datetime.now()} - Shield Active")

    ip_counts = {}
    with open(LOG_FILE, "r") as f:
        for line in f:
            if "Failed password" in line:
                ip = line.split()[-4]
                ip_counts[ip] = ip_counts.get(ip, 0) + 1

    for ip, count in ip_counts.items():
        if count >= THRESHOLD:
            country = get_geo_info(ip)
            blocked = block_ip(ip)

#Structured JSON Logging
            event = {
                "timestamp": str(datetime.now()),
                "ip": ip,
                "count": count,
                "country": country,
                "action": "BLOCKED" if blocked else "ALREADY_BLOCKED"
        }
            with open(JSON_LOG, "a") as f:
                f.write(json.dumps(event) + "\n")
            if blocked:
                print(f"[!] CRITICAL: Blocked {ip} ({country}) - {count} attempts")

if __name__ == "__main__":
    while True:
        try:
            run_sentinel()
            print("[*] Scan complete. Sleeping for 60 seconds..")
            time.sleep(60)
        except Exception as e:
            print(f"[!] System Error: {e}")
            time.sleep(10)



