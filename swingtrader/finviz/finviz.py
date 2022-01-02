# Copyright (c) 2021-2022 Kabylkas Labs.
# Licensed under the Apache License, Version 2.0.
import finviz.finvizimpl as finvizimpl

class Finviz:
    def GetCurrentPrice(self, ticker):
        return finvizimpl.GetCurrentPrice(ticker)