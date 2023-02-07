# This is a sample Python script.
from enum import Enum

class Suit(Enum):
    Hearts = 4
    Spades = 3
    Clubs = 2
    Diamonds = 1


print(Suit.Hearts)

print(Suit.Hearts.value)

class PlayingCard(Suit):
    __init__(self, )
