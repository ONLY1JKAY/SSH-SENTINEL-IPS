log_file = open("/var/log/auth.log", "r")

for line in log_file:
  if "Failed password" in line:
   print(line)

log_file.close()
