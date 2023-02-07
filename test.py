from enum import Enum


# class syntax
class Suit(Enum):
    Hearts = 4
    Spades = 3
    Clubs = 2
    Diamonds = 1


# functional syntax
print(type(Suit.Hearts))
