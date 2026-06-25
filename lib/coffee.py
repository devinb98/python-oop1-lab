#!/usr/bin/env python3

class Coffee:
    def __init__(self, size: str, price: float):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in {"Small", "Medium", "Large"}:
            print("size must be Small, Medium, or Large")
            return
        self._size = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            print("price must be a number")
            return
        self._price = value

    def brew(self):
        print(f"Brewing a cup of {self.size} coffee...")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1