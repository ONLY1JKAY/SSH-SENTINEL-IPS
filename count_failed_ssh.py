log_file = open("/var/log/auth.log", "r")

failed_count = 0

for line in log_file:
  if "Failed password" in line:
    failed_count += 1

log_file.close()

print("Total failed login SSH attempts:", failed_count)
