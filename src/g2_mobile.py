import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Replace with Bright Data credentials
customer_id = "<customer_id>"
zone_name = "<zone_name>"
zone_password = "<zone_password>"

# Proxy details
proxy_url = f"http://brd-customer-{customer_id}-zone-{zone_name}-ua-mobile:{zone_password}@brd.superproxy.io:33335"
proxies = {"http": proxy_url, "https": proxy_url}

url = "https://www.g2.com/products/mongodb/reviews"

try:
    response = requests.get(url, proxies=proxies, verify=False)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    headings = [h3.get_text(strip=True) for h3 in soup.find_all("h3")]
    print("\nExtracted <h3> Headings:" if headings else "No <h3> headings found.")
    print(*headings, sep="\n- ")
except requests.RequestException as e:
    print(f"Error: {e}")
