# Copyright (c) 2021-2022 Kabylkas Labs.
# Licensed under the Apache License, Version 2.0.

# Python packages.
import requests
from bs4 import BeautifulSoup

# Local packages.
import finviz.constants as constants

# Helper functions.
def get_content(url):
    req = requests.get(url, headers = constants.kHtmlHeader)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup

# Implementation methods of the API.
def GetCurrentPrice(ticker):
    url = constants.kFinvizQuoteUrl.format(ticker)
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