# Copyright (c) 2021-2022 Kabylkas Labs.
# Licensed under the Apache License, Version 2.0.
import stockmarketapi

def main():
    amd_stock = stockmarketapi.Stock("FB")
    print(amd_stock.GetCurrentPrice())
    print(amd_stock.GetROIC())

main()