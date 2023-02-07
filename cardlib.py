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



class NumberedCard(PlayingCard):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        
class JackCard(PlayingCard):

class QueenCard(PlayingCard):

class KingCard(PlayingCard):

class AceCard(PlayingCard):




