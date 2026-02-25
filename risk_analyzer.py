def calculate_risk(ip, count, geo_data):
    # Logic: High risk if attempts > 3 OR from a specific region
    # You can expand this logic easily later!
    score = count * 10
    
    if geo_data['country'] in ["Russia", "China", "North Korea", "India"]:
        score += 50
    
    if score >= 30:
        return "High", score
    elif score >= 15:
        return "Medium", score
    return "Low", score
