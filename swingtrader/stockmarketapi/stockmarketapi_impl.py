# Copyright (c) 2021-2022 Kabylkas Labs.
# Licensed under the Apache License, Version 2.0.

# Python packages.
import requests
from bs4 import BeautifulSoup

# Local packages.
import stockmarketapi.constants as constants

# Helper functions.
def GetContent(url):
    req = requests.get(url, headers = constants.kHtmlHeader)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup

# Implementation methods of the API.
def GetCurrentPrice(ticker):
    url = constants.kFinvizQuoteUrl.format(ticker)
    soup = GetContent(url)
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

def GetROIC(ticker):
    url = constants.kGuruFocusRoicUrl.format(ticker)
    soup = GetContent(url)
    roic_div = soup.find("div", { "id": "target_def_description" })
    strongs = roic_div.find_all("strong")

    strong = "{}".format(strongs[3])
    parse_stage_1 = strong.split("<strong>")
    parse_stage_2 = parse_stage_1[1].split("%")
    roic = parse_stage_2[0]

    return float(roic)

def LoadMarket():
    print("Loading market...")
    market_tickers = []    
    url = constants.kFinvizEmptyScreenerUrl
    next_found = True
    pages_parsed = 0
    while next_found:
        print("Parsing {}".format(url))
        soup = GetContent(url)

        # Get the anchor that links to the next page.
        all_links = soup.find_all("a", { "class" : "tab-link"})
        next_found = False
        for link in all_links:
            string_link = "{}".format(link)
            if "next" in string_link:
                next_found = True
                s = string_link.split("\"")
                save_link = s[3]
                save_link = save_link.replace("&amp;", "&")

        if next_found:
            url = "https://finviz.com/{}".format(save_link)

        # Get the tickers.
        screener_content_div = soup.find("div", { "id" : "screener-content"} )
        ticker_links = screener_content_div.find_all("a", { "class" : "screener-link-primary"})
        for link in ticker_links:
            string_link = "{}".format(link)
            s_0 = string_link.split("?t=")
            s_1 = s_0[1].split("&")[0]
            market_tickers.append(s_1)

        # Increment the count.
        pages_parsed += 1

        
    print("Pages parsed: {}".format(pages_parsed + 1))
    print(market_tickers)
    return market_tickers