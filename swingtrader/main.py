# Copyright (c) 2021-2022 Kabylkas Labs.
# Licensed under the Apache License, Version 2.0.
import finviz

def main():
    finviz_api = finviz.Finviz()
    print(finviz_api.GetCurrentPrice("AMD"))

main()