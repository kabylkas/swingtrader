# Copyright (c) 2021-2022 Kabylkas Labs.
# Licensed under the Apache License, Version 2.0.
import finviz

def main():
    a = finviz.Finviz()
    print(a.GetCurrentPrice("AMD"))

main()