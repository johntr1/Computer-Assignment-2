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
        if self.get_value() == other.get_value():
            return self.suit.value < other.suit.value
        else:
            return self.get_value() < other.get_value()

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
        return 14


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
                if self.cards[j] > self.cards[j + 1]:
                    self.cards[j], self.cards[j + 1] = self.cards[j + 1], self.cards[j]
                    is_swapped = True

            if not is_swapped:
                return

    def drop_cards(self, drop_list):
        # Reverse the index list to prevent change of indexes in the card_list
        drop_list = sorted(drop_list, reverse=True)
        for i in drop_list:
            del self.cards[i]



class PokerHand:
    def __init__(self, cards, value):
        self.cards = cards
        self.value = []

    def get_value(self, cards):
        check= self.check_straight_flush(self)
        if not check==None:
            return [9] + check

        count=self.get_count(self.cards)
        check=self.check_four_of_a_kind(self, count)
        if not check==None:
            return [8]+check

        check = self.check_full_house(self, count)
        if not check == None:
            return [7] + check

        check = self.check_flush(self)
        if not check == None:
            return [6] + check

        check = self.check_straight(self)
        if not check == None:
            return [5] + check

        check = self.check_three_of_a_kind(self)
        if not check == None:
            return [4] + check

        check = self.check_two_pair(self)
        if not check == None:
            return [3] + check

        check = self.check_pair(self)
        if not check == None:
            return [2] + check


        return [1] + self.its_high_cards(self)

        #och så fortsätter den att testa alla, har inte gjort en för high cards på den behöver return vara
        #card value och suit






    def check_straight_flush(self):
        """
        Checks for the best straight flush in a list of cards

        :return:
        """
        #works if ace is sett as 14
        for c in self.cards:
            if c.get_value()==14:
                self.cards.append((1,c.suit))

        for card in reversed(self.cards):
            for k in range(1, 5):
                if (card.get_value()-k , card.suit) not in self.cards:
                    break
            straight_flush=True
            if straight_flush:
                return [card.get_value(), card.suit]


    def get_count(self):
        count = [0] * len(self.cards)
        # Two for loops to count how many of the same value exists and where
        for i, card1 in enumerate(self.cards):
            for card2 in self.cards:
                if card1.get_value() == card2.get_value():
                    count[i] = count[i] + 1
        return count


    def check_four_of_a_kind(self,count):
        #finds the posiontion of the three of a kinda and gets the highest card
        if 4 in count:
            four_indices=[i for i, x in enumerate(count) if x==4]
            the_fours=self.cards[four_indices]
            the_fours=reversed(the_fours.sort())
            return the_fours[0].get_value()

    def check_full_house(self, count):
        if 2 in count and 3 in count:
            #Finds the position of the three of a kind and get what value it has
            threes_indices=[i for i, x in enumerate(count) if x==3]
            threes=self.cards[threes_indices]
            threes=reversed(threes.sort())
            return threes[0].get_value()


    def check_flush(self):
        suit_count = [0] * len(Suit)
        # Two for loops to count how many of the same value exists and where
        for i, card1 in enumerate(self.cards):
            for card2 in self.cards:
                if card1.get_value() == card2.get_value():
                    suit_count[i] = suit_count[i] + 1
        return count
    def check_straight(self):
        for c in self.cards:
            if c.get_value()==14:
                self.cards.append((1,c.suit))

        for card in reversed(self.cards):
            for k in range(1, 5):
                if (card.get_value()-k) not in self.cards:
                    break
            straight=True
            if straight:
                return [card.get_value(), card.suit]

    def check_three_of_a_kind(self, count):
        if 3 in count:
        # Finds the position of the three of a kind and get what value it has
            threes_indices = [i for i, x in enumerate(count) if x == 3]
            threes = self.cards[threes_indices]
            threes = reversed(threes.sort())
            return threes[0].get_value()

    def check_two_pair(self, count):
         if len([i for i in count if i==2]) >= 2:
            # Finds the position of the pars of a kind and get what value and suit it has
            pair_indices=[i for i, x in enumerate(count) if x==2]
            pairs=self.cards[pair_indices]
            pairs=reversed(pairs.sort())
            return pairs[0].get_value(), pairs[0].suit

    def check_pair(self, count):
        if 2 in count:
# Finds the position of the pars of a kind and get what value and suit it has
            pair_indices=[i for i, x in enumerate(count) if x==2]
            pair=self.cards[pair_indices]
            pair=reversed(pair.sort())
            return pair[0].get_value(), pair[0].suit

    def its_high_cards(self):
        cards=reversed(self.cards.sort())
        return cards[0].get_value(), cards[0].suit






h = Hand()
d = StandardDeck()
d.shuffle()
for i in range(20):
    h.add_card(d.draw())

for i in range(len(h.cards)):
    print(h.cards[i])
h.sort()
print('splitt')
for i in range(len(h.cards)):
    print(h.cards[i])
dl = [0, 2]
print('splitt')

for i in range(len(h.cards)):
    print(h.cards[i])

print(PokerHand.check_full_house_three_2pair_pair(h))