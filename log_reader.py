log_file = open("/var/log/auth.log", "r")

for line in log_file:
  print(line)

log_file.close()
