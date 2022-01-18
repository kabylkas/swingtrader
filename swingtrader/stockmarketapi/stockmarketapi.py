# Copyright (c) 2021-2022 Kabylkas Labs.
# Licensed under the Apache License, Version 2.0.
import stockmarketapi.stockmarketapi_impl as impl

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.price = 0
        self.roic = 0.0

    def GetCurrentPrice(self):
        return impl.GetCurrentPrice(self.ticker)

    def GetROIC(self):
        return impl.GetROIC(self.ticker)

class Market:
    def __init__(self):
        self.all_tickers = []

    def LoadMarket(self):
        self.all_tickers = impl.LoadMarket()