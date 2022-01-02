# Copyright (c) 2021-2022 Kabylkas Labs.
# Licensed under the Apache License, Version 2.0.

class Trader:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.cash_balance = 0.0
        self.positions = []

    def LoadInfo(self, path_to_json):
