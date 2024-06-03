import requests
import re

url = "https://xat.com/web_gear/chat/auser3.php"

def run() -> None:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.text
        user_id_match = re.search(r'&UserId=(\d+)&', text)
        k1_match = re.search(r'&k1=([\w\d]+)&', text)
        k2_match = re.search(r'&k2=([\w\d]+)', text)
        
        if user_id_match:
            print("UserId:", user_id_match.group(1))
        else:
            print("UserId not found")
        
        if k1_match:
            print("k1:", k1_match.group(1))
        else:
            print("k1 not found")
        
        if k2_match:
            print("k2:", k2_match.group(1))
        else:
            print("k2 not found")

        # Optionally, print the full text for manual inspection
        # print(text)
    else:
        print("Failed to fetch page")

run()
