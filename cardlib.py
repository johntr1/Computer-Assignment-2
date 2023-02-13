# This is a sample Python script.
from enum import Enum
from abc import ABCMeta, abstractmethod
import random


class Suit(Enum):
    Hearts = 4
    Spades = 3
    Clubs = 2
    Diamonds = 1

    def __str__(self):
        return self.name


class PlayingCard(metaclass=ABCMeta):
    def __init__(self, suit):
        self.suit = suit

    @abstractmethod
    def get_value(self):
        pass

    def __lt__(self, other):
        if self.suit.value == other.suit.value:
            return self.get_value() < other.get_value()
        else:
            return self.suit.value < other.suit.value

    def __eq__(self, other):
        if self.get_value() == other.get_value() and self.suit.value == other.suit.value:
            return True
        else:
            return False


class NumberedCard(PlayingCard):
    def __init__(self, value, suit):
        super().__init__(suit)
        self.value = value

    def __str__(self):
        return f'{self.value} of {self.suit}'

    def get_value(self):
        return self.value


class JackCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def __str__(self):
        return f' Jack of {self.suit}'

    def get_value(self):
        return 11


class QueenCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def __str__(self):
        return f' Queen of {self.suit}'

    def get_value(self):
        return 12


class KingCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def __str__(self):
        return f' King of {self.suit}'

    def get_value(self):
        return 13


class AceCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def __str__(self):
        return f' Ace of {self.suit}'

    def get_value(self):
        return 1




# StandardDeck
class StandardDeck:
    def __init__(self):
        self.deck = []
        for i in Suit:
            self.deck.append(AceCard(i))
            for j in range(2, 11):
                self.deck.append(NumberedCard(j, i))
            self.deck.append(JackCard(i))
            self.deck.append(QueenCard(i))
            self.deck.append(KingCard(i))

    def draw(self):
        return self.deck.pop(0)

    def shuffle(self):
        return random.shuffle(self.deck)


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, draw):
        self.cards.append(draw)

    def sort(self):
        n = len(self.cards) - 1  # Reduces the length by -1 to avoid an extra loop at the end
        # Implementation of Bubble Sort
        is_swapped = False  # Optimization to later check if list is already swapped

        for i in range(n):
            for j in range(n - i):
                if self.cards[j].get_value() > self.cards[j + 1].get_value():
                    self.cards[j] = self.cards[j + 1]
                    self.cards[j + 1] = self.cards[j]

            if not is_swapped:
                return


h = Hand()
d = StandardDeck()
d.shuffle()
h.add_card(d.draw())
h.add_card(d.draw())
h.add_card(d.draw())
h.add_card(d.draw())
h.add_card(d.draw())
h.sort()
print(h.cards)

for i in range(len(h.cards)):
    print(h.cards[i])


# def shuffle(self):

# def draw(self):
