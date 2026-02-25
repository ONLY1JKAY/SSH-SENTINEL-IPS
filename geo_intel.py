import requests

def get_geo_info(ip):
    try:
        # We use ip-api.com as you had in your script
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if response.get('status') == 'success':
            return {
                "country": response.get('country', 'Unknown'),
                "isp": response.get('isp', 'Unknown')
            }
    except Exception:
        pass
    return {"country": "Unknown", "isp": "Unknown"}
