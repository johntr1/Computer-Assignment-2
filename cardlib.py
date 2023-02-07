# This is a sample Python script.
from enum import Enum
from abc import ABCMeta, abstractmethod
class Suit(Enum):
    Hearts = 4
    Spades = 3
    Clubs = 2
    Diamonds = 1


print(Suit.Hearts)

print(Suit.Hearts.value)

class PlayingCard(metaclass=ABCMeta):

    @abstractmethod
    def get_value(self):
        return self.value



class NumberedCard(PlayingCard):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def __lt__(self, other):
        if self.get_value() == other.get_value():
            return self.suit.value < other.suit.value
        else:
            return self.get_value() < other.get_value()

class JackCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value(self):
        return 11


class QueenCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value(self):
        return 12

class KingCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value(self):
        return 13

    def __lt__(self, other):
        if self.get_value() == other.get_value():
            return self.suit.value < other.suit.value
        else:
            return self.get_value() < other.get_value()



class AceCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit



print(NumberedCard(4, Suit.Hearts))