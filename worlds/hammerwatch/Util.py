import typing
from enum import Enum


class Campaign(Enum):
    Castle = 0
    Temple = 1


class Counter:
    def __init__(self, start: int = 0):
        self.counter = start

    def count(self, amount: int = 1):
        self.counter += amount
        return self.counter
