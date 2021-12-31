import requests
from bs4 import BeautifulSoup

h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_content(url):
    req = requests.get(url, headers = h)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup

def scrape_screener(url):
    soup = get_content(url)
    screener_content = soup.find("div", { "id": "screener-content" })
    links = screener_content.find_all("a", { "class": "screener-link-primary" })

def get_current_price(ticker):
    url = "https://finviz.com/quote.ashx?t={}".format(ticker)
    soup = get_content(url)
    all_content = soup.find("div", { "data-testid": "quote-data-content" })
    table_content = all_content.find_all("td")

    found_price = False
    price_element = ""
    for data in table_content:
        if found_price:
            price_element = "{}".format(data)
            break

        if "Price" in data:
            found_price = True 

    parse_stage_1 = price_element.split("<b>")
    parse_stage_2 = parse_stage_1[1].split("</b>")
    price = parse_stage_2[0]

    return float(price)
    

#screener_url = "https://finviz.com/screener.ashx?v=111&f=cap_midover,sh_avgvol_o750,sh_curvol_o1000,sh_price_o15,ta_averagetruerange_o1,ta_sma20_pc&ft=4"
#scrape_screener(screener_url)

print(get_current_price("AMD"))
print(get_current_price("FB"))
print(get_current_price("HIMX"))
