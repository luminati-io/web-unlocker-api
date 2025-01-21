# Web Unlocker API

[![Promo](https://github.com/luminati-io/LinkedIn-Scraper/raw/main/Proxies%20and%20scrapers%20GitHub%20bonus%20banner.png)](https://brightdata.com/) 

[Web Unlocker](https://brightdata.com/products/web-unlocker) is a powerful scraping API that allows access to any website while bypassing sophisticated bot protections. You can retrieve clean HTML/JSON responses with a single API call without managing complex anti-bot infrastructure.

# Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
   - [Direct API Access](#direct-api-access)
   - [Native Proxy-Based Access](#native-proxy-based-access)
- [Practical Example: Scraping G2 Reviews](#practical-example-scraping-g2-reviews)
   - [Basic Request (Without Web Unlocker)](#basic-request-without-web-unlocker)
   - [Enhanced Request (With Web Unlocker)](#enhanced-request-with-web-unlocker)
      - [Direct API Access](#direct-api-access)
      - [Proxy-Based Access](#proxy-based-access)
      - [Waiting for Specific Elements](#waiting-for-specific-elements)
      - [Mobile User-Agent Targeting](#mobile-user-agent-targeting)
      - [Geolocation Targeting](#geolocation-targeting)
      - [Debugging Requests](#debugging-requests)
      - [Success Rate Statistics](#success-rate-statistics)
- [Final Notes](#final-notes)

## Features
Web Unlocker provides comprehensive web scraping capabilities:
- Automatic proxy management and CAPTCHA solving
- Real-user behavior simulation
- Built-in JavaScript rendering
- Global geo-targeting
- Automated retry mechanisms
- Pay-per-success pricing model

## Getting Started
Before using Web Unlocker, complete the setup by following the [quickstart guide](https://docs.brightdata.com/scraping-automation/web-unlocker/quickstart).

### Direct API Access
The recommended method for integrating Web Unlocker.


**Example: cURL Command**
```bash
curl -X POST "https://api.brightdata.com/request" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer INSERT_YOUR_API_TOKEN" \
-d '{
  "zone": "INSERT_YOUR_WEB_UNLOCKER_ZONE_NAME",
  "url": "http://lumtest.com/myip.json",
  "format": "raw"
}'
```

1. API Endpoint: `https://api.brightdata.com/request`
2. Authorization Header: Your [API token](https://docs.brightdata.com/scraping-automation/web-unlocker/send-your-first-request#generating-your-bright-data-api-token) from the Web Unlocker API zone
3. Payload:
   - `zone`: Your Web Unlocker API zone name
   - `url`: Target URL to access
   - `format`: Response format (use `raw` for direct site response)

**Example: Python Script**
```python
import requests

API_URL = "https://api.brightdata.com/request"
API_TOKEN = "INSERT_YOUR_API_TOKEN"
ZONE_NAME = "INSERT_YOUR_WEB_UNLOCKER_ZONE_NAME"
TARGET_URL = "http://lumtest.com/myip.json"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

payload = {
    "zone": ZONE_NAME,
    "url": TARGET_URL,
    "format": "raw"
}

response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code == 200:
    print("Success:", response.text)
else:
    print(f"Error {response.status_code}: {response.text}")
```

### Native Proxy-based Access

Alternative method using proxy-based routing.

**Example: cURL Command**
```bash
curl "http://lumtest.com/myip.json" \
--proxy "brd.superproxy.io:33335" \
--proxy-user "brd-customer-<CUSTOMER_ID>-zone-<ZONE_NAME>:<ZONE_PASSWORD>"
```

Required credentials:
1. Customer ID: Found in [Account settings](https://brightdata.com/cp/setting/customer_details)
2. Web Unlocker API zone name: Found in the overview tab
3. Web Unlocker API password: Found in the overview tab

**Example: Python Script**
```python
import requests

customer_id = "<customer_id>"
zone_name = "<zone_name>"
zone_password = "<zone_password>"

host = "brd.superproxy.io"
port = 33335
proxy_url = f"http://brd-customer-{customer_id}-zone-{zone_name}:{zone_password}@{host}:{port}"

proxies = {"http": proxy_url, "https": proxy_url}

response = requests.get("http://lumtest.com/myip.json", proxies=proxies)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
```

## Practical Example: Scraping G2 Reviews
Let's see how to scrape reviews from [G2.com](https://www.g2.com/), a site heavily protected by Cloudflare.

### Basic Request (Without Web Unlocker)
Using a simple Python script to scrape [G2 reviews](https://www.g2.com/products/mongodb/reviews):
```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.g2.com/products/mongodb/reviews'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    headings = soup.find_all('h2')
    
    if headings:
        print("\nHeadings Found:")
        for heading in headings:
            print(f"- {heading.get_text(strip=True)}")
    else:
        print("No headings found")
else:
    print("Request blocked")
```

**Result:** The script fails (`403` error) due to Cloudflare’s anti-bot measures.


### Enhanced Request (With Web Unlocker)
To bypass such restrictions, use Web Unlocker. Below is a Python implementation:

#### Direct API Access
```python
import requests
from bs4 import BeautifulSoup

API_URL = "https://api.brightdata.com/request"
API_TOKEN = "INSERT_YOUR_API_TOKEN"
ZONE_NAME = "INSERT_YOUR_ZONE"
TARGET_URL = "https://www.g2.com/products/mongodb/reviews"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}
payload = {"zone": ZONE_NAME, "url": TARGET_URL, "format": "raw"}

response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    headings = [h.get_text(strip=True) for h in soup.find_all('h2')]
    print("\nExtracted Headings:", headings)
else:
    print(f"Error {response.status_code}: {response.text}")
```
**Result:** Successfully bypasses protection, retrieves content with status `200`.

#### Proxy-Based Access
Alternatively, use the proxy-based method:
```python
import requests
from bs4 import BeautifulSoup

proxy_url = "http://brd-customer-<customer_id>-zone-<zone_name>:<zone_password>@brd.superproxy.io:33335"
proxies = {"http": proxy_url, "https": proxy_url}

url = "https://www.g2.com/products/mongodb/reviews"
response = requests.get(url, proxies=proxies, verify=False)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    headings = [h.get_text(strip=True) for h in soup.find_all('h2')]
    print("\nExtracted Headings:", headings)
else:
    print(f"Error {response.status_code}: {response.text}")
```

**Note:** Suppress SSL certificate warnings by adding:
```python
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
```

#### Waiting for Specific Elements
Use the `x-unblock-expect` header to wait for specific elements or text:
```python
headers["x-unblock-expect"] = '{"element": ".star-wrapper__desc"}'
# or
headers["x-unblock-expect"] = '{"text": "reviews"}'
```

👉 You can find the complete code in [g2_wait.py](https://github.com/luminati-io/web-unlocker/blob/main/src/g2_wait.py)

#### Mobile User-Agent Targeting
To use mobile user agents instead of desktop ones, append `-ua-mobile` to your username:
```python
username = f"brd-customer-{customer_id}-zone-{zone_name}-ua-mobile"
```
👉 You can find the complete code in [g2_mobile.py](https://github.com/luminati-io/web-unlocker/blob/main/src/g2_mobile.py)

#### Geolocation Targeting
While Web Unlocker automatically selects optimal IP locations, you can specify target locations:
```python
username = f"brd-customer-{customer_id}-zone-{zone_name}-country-us"
username = f"brd-customer-{customer_id}-zone-{zone_name}-country-us-city-sanfrancisco"
```

👉 You can learn more [here](https://docs.brightdata.com/api-reference/proxy/geolocation-targeting).

#### Debugging Requests
Enable detailed debugging information by adding the `-debug-full` flag:
```python
username = f"brd-customer-{customer_id}-zone-{zone_name}-debug-full"
```
👉 You can find the complete code in [g2_debug.py](https://github.com/luminati-io/web-unlocker/blob/main/src/g2_debug.py)

#### Success Rate Statistics
Monitor API success rates for specific domains:
```python
import requests

API_TOKEN = "INSERT_YOUR_API_TOKEN"

def get_success_rate(domain):
    url = f"https://api.brightdata.com/unblocker/success_rate/{domain}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    print(response.json() if response.status_code == 200 else response.text)

get_success_rate("g2.com") # Get statistics for specific domain
get_success_rate("g2.*") # Get statistics for all top-level domains
```

## Final Notes
Web Unlocker lets you scrape even the most protected websites effortlessly. Key points to remember:

1. **Not Compatible With**:  
   - Browsers (Chrome, Firefox, Edge)  
   - Anti-detect browsers (Adspower, Multilogin)  
   - Automation tools (Puppeteer, Playwright, Selenium)  

2. **Use Scraping Browser**:  
   For browser-based automation, use Bright Data’s [Scraping Browser](https://docs.brightdata.com/scraping-automation/scraping-browser/introduction).

3. **Premium Domains**:  
   Access challenging sites with [premium domain](https://docs.brightdata.com/scraping-automation/web-unlocker/features#web-unlocker-api-premium-domains) features.

4. **CAPTCHA Solving**:  
   Solved automatically, but can be [disabled](https://docs.brightdata.com/scraping-automation/web-unlocker/features#disable-captcha-solving).
   
5. **Custom Headers & Cookies**:  
   Send your own to target specific site versions. [Learn more](https://docs.brightdata.com/scraping-automation/web-unlocker/features#manual-headers-and-cookies).

Visit the [official documentation](https://docs.brightdata.com/scraping-automation/web-unlocker/introduction) for more details.
