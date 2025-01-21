import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Bright Data credentials and proxy details
customer_id = "<customer_id>"
zone_name = "<zone_name>"
zone_password = "<zone_password>"
proxy_url = f"http://brd-customer-{customer_id}-zone-{zone_name}-debug-full:{zone_password}@brd.superproxy.io:33335"
proxies = {"http": proxy_url, "https": proxy_url}

# Target URL
url = "https://www.g2.com/products/mongodb/reviews"

try:
    response = requests.get(url, proxies=proxies, verify=False)
    response.raise_for_status()

    print(f"Request Successful! Status Code: {response.status_code}")

    # Debugging information from headers
    debug_info = response.headers.get("x-brd-debug")
    if debug_info:
        print("\nDebug Information:")
        print(debug_info)

    # Extract and print <h2> headings
    soup = BeautifulSoup(response.text, "lxml")
    headings = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
    print("\nExtracted <h2> Headings:" if headings else "No <h2> headings found.")
    print(*headings, sep="\n- ")
except requests.RequestException as e:
    print(f"Error: {e}")
