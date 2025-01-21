import requests
from bs4 import BeautifulSoup

API_URL = "https://api.brightdata.com/request"
API_TOKEN = "INSERT_YOUR_API_TOKEN"
ZONE_NAME = "INSERT_YOUR_ZONE"
TARGET_URL = "https://www.g2.com/products/mongodb/reviews"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}",
    "x-unblock-expect": '{"element": ".star-wrapper__desc"}',
}

payload = {"zone": ZONE_NAME, "url": TARGET_URL, "format": "raw"}

response = requests.post(API_URL, headers=headers, json=payload)

if response.ok:
    soup = BeautifulSoup(response.text, "lxml")
    headings = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
    print("\nExtracted <h2> Headings:" if headings else "No <h2> headings found.")
    print(*headings, sep="\n- ")
else:
    print(f"Error {response.status_code}: {response.text}")
