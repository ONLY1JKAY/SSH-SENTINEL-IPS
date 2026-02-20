import requests
test_ip = "8.8.8.8"
url = f"http://ip-api.com/json/{test_ip}"
response = requests.get(url).json()

if response['status'] == 'success':
    print(f"Intelligence for {test_ip}:")
    print (f"Country: {response['country']}")
    print(f"City: {response['city']}")
    print(f"ISP: {response['isp']}")
else:
    print("Could not retrieve data for this IP.")
