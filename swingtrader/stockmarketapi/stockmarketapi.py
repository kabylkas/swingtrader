# Copyright (c) 2021-2022 Kabylkas Labs.
# Licensed under the Apache License, Version 2.0.
import stockmarketapi.stockmarketapi_impl as impl

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker

    def GetCurrentPrice(self):
        return impl.GetCurrentPrice(self.ticker)