import typing


class Counter:
    def __init__(self, start: int):
        self.counter = start

    def count(self, amount: int = 1):
        self.counter += amount
        return self.counter - amount
