import typing


class Counter:
    def __init__(self, start: int):
        self.counter = start

    def count(self):
        self.counter += 1
        return self.counter - 1