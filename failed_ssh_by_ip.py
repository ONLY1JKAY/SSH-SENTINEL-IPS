import re
from collections import Counter

log_path = "/var/log/auth.log"
ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')

failed_ips = []

try:
    with open(log_path, "r") as f:
        for line in f:
            if "Failed password" in line:
                match = ip_pattern.search(line)
                if match:
                    failed_ips.append(match.group())

    ip_counts = Counter(failed_ips)

    print(f"{'IP Address':<20} | {'Attempts'}")
    print("-" * 30)
    for ip, count in ip_counts.most_common():
        print(f"{ip:<20} | {count}")

except FileNotFoundError:
    print("Error: Could not ind auth.log. Are you running this on linux with sudo?")
