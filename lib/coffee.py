#!/usr/bin/env python3

class Coffee:
    def __init__(self, size: str, price: float):
        if size not in {"Small", "Medium", "Large"}:
            print("size must be Small, Medium, or Large")
        self.size = size
        self.price = price

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1