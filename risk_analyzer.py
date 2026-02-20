log_file = open("/var/log/auth.log", "r")
ip_counts = {}

for line in log_file:
    if "Failed password" in line:
        parts = line.split()
        ip = parts[-4]
        ip_counts[ip] = ip_counts.get(ip, 0) + 1
log_file.close()

print(f"{'STATUS':<15} | {'IP ADDRESS':<15} | {'ATTEMPTS'}")
print("-" * 50)

for ip, count in ip_counts.items():
    if count > 50:
        status = "CRITICAL !!"
    elif count > 10:
        status = "WARNING"
    else:
        status = "LOW"

    print(f"{status:<15} | {ip:<15} | {count}")
