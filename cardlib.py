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
        self.poker_hand = None
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

    def best_poker_hand(self, cards):
        self.cards = self.cards + cards
        self.cards.sort()
        poker_hand = PokerHand(self.cards)
        return poker_hand

    #  if self.best_poker_hands(cards) == 1 and other.best_poker_hands(cards) == 1
class HandType(Enum):
    STRAIGHT_FLUSH = 9
    FOUR_OF_A_KIND = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH_CARD = 1


class PokerHand:
    def __init__(self, cards):
        self.cards = cards

    def __lt__(self, other):
        self_tuple = self.check_poker_hand_value()
        other_tuple = other.check_poker_hand_value()

        # Uses tuple comparison to quickly compare two hands
        # The tuples are ordered in such way that the first element in the tuple is the hand type rank
        # The following elements are card values or suit values to compare same type of hands.
        # The order is determined by the given Wikipedia page by the assignment
        if self_tuple < other_tuple:
            return self_tuple < other_tuple

    def __eq__(self, other):
        # There is a draw for straight hand according to Wikipedia where the tuples be equal to each other
        self_tuple = self.check_poker_hand_value()
        other_tuple = other.check_poker_hand_value()
        if self_tuple == other_tuple:
            return True
        else:
            return False

    def __str__(self):
        return HandType(self.check_poker_hand_value()[0]).name

    def check_poker_hand_value(self):
        """
        Checks the value of the poker hand by using all check functions

        :param: self

        :return: (tuple): The poker hand's value described in a tuple.
        """

        # Get the amount of same type of cards and its position
        count = self.get_count()

        # Following code in the function will check if the functions return a value or None
        # If true, returns a tuple with the initial value being predetermined hand type rank and check
        check = self.check_straight_flush()
        if check is not None:
            return (HandType.STRAIGHT_FLUSH.value,) + check

        check = self.check_four_of_a_kind(count)
        if check is not None:
            return (HandType.FOUR_OF_A_KIND.value,) + check

        check = self.check_full_house(count)
        if check is not None:
            return (HandType.FULL_HOUSE.value,) + check

        check = self.check_flush()
        if check is not None:
            return (HandType.FLUSH.value,) + check

        check = self.check_straight()
        if check is not None:
            return (HandType.STRAIGHT.value,) + check

        check = self.check_three_of_a_kind(count)
        if check is not None:
            return (HandType.THREE_OF_A_KIND.value,) + check

        check = self.check_two_pair(count)
        if check is not None:
            return (HandType.TWO_PAIR.value,) + check

        check = self.check_pair(count)
        if check is not None:
            return (HandType.PAIR.value,) + check
        else:
            check = self.its_high_cards()
            return (HandType.HIGH_CARD.value,) + check

    def check_straight_flush(self):
        """
        Checks for the best straight flush in a list of cards

        if it's a straight flush
        :return (tuple): The value of highest card in the straight flush
        if not
        :return (NoneType): None
        """
        # Makes a list of tuples from card objects
        cards = [(card.get_value(), card.suit) for card in self.cards]
        ace_cards = [(1, card.suit) for card in self.cards if card.get_value() == 14]

        cards = ace_cards + cards
        cards = list(reversed(cards))
        for i, card in enumerate(cards):
            for k in range(1, 5):
                straight_flush = True
                if (card[0] - k, card[1]) not in cards:
                    straight_flush = False
                    break
            if straight_flush:
                return card[0],

    def get_count(self):
        """

        :param: self
        :return: count
        """
        count = [0] * len(self.cards)
        # Two for loops to count how many of the same value exists and where they are index
        for i, card1 in enumerate(self.cards):
            for card2 in self.cards:
                if card1.get_value() == card2.get_value():
                    count[i] = count[i] + 1
        return count

    def check_four_of_a_kind(self, count):
        """
        Checks for the highest four of a kind in a list of cards

        if it has four of a kind it
        :return (tuple): The value of highest four of a kind then the highest card value of the kickers
        if not
        :return (NoneType): None
        """
        if 4 in count:
            # gets the indices for the four of a kinda and the kicker
            four_indices = [i for i, x in enumerate(count) if x == 4]
            kicker_indices = [i for i, x in enumerate(count) if x != 4]
            # creates two lists for the fours and the kickers
            kicker = [self.cards[x] for x in kicker_indices]
            the_fours = [self.cards[x] for x in four_indices]
            # Returns the value of the fours and the highest card from the kickers
            return the_fours[-1].get_value(), kicker[-1].get_value()

    def check_full_house(self, count):
        """
        Checks for the highest full house in a list of cards

        if the list has a full house
        :return (tuple): The value of highest three of a kind then the value for the highest pair
        if not
        :return (NoneType): None
        """
        if 2 in count and 3 in count:
            # Finds the position of the three of a kind and get what the highets value it has
            threes_indices = [i for i, x in enumerate(count) if x == 3]
            threes = [self.cards[x] for x in threes_indices]  # Returns elements from list of indices

            # Finds the position of the twos and its value
            two_indices = [i for i, x in enumerate(count) if x == 2]
            twos = [self.cards[x] for x in two_indices]
            return threes[-1].get_value(), twos[-1].get_value()

    def check_flush(self):
        """
        Checks for the best flush in a list of cards

        if it's a flush
        :return (tuple): The value of highest card in the flush then the next highest and repeats to the lowest card
        if not
        :return (NoneType): None
        """
        # Create a list of the cards' suits
        suits = [self.cards[x].suit for x, e in enumerate(self.cards)]
        #  Dictionary with amount of suits and the suit_name that occurs in the list
        suit_count = {suit_name: suits.count(suit_name) for suit_name in sorted(set(suits), key=suits.index)}
        # Loop that checks for every suit if its value is >= 5 and returns max value of that suit and its suit.
        for suit_name, value in suit_count.items():
            if value >= 5:
                suit_list = [card for idx, card in enumerate(self.cards) if card.suit == suit_name]
                return suit_list[-1].get_value(), suit_list[-2].get_value(), suit_list[-3].get_value(), \
                    suit_list[-4].get_value(), suit_list[-5].get_value()

    def check_straight(self):
        """
        Checks for the best straight in a list of cards

        if it's a straight
        :return (tuple): The value of highest card in the flush then the next highest and repeats to the lowest card
        if not
        :return (NoneType): None
        """
        # Create a list with the cards' values in rank
        values = [x.get_value() for idx, x in enumerate(self.cards)]
        if 14 in values:
            values = [1] + values
        # Remove of the same rank:
        values = sorted(set(values), key=values.index)
        counter = 0
        li = []
        # Iterates through the values
        for i in range(len(values) - 1):
            # If the difference is 1 add to the counter and append the value to list
            if values[i + 1] - values[i] == 1:
                counter += 1
                li.append(values[i + 1])
            elif counter < 4:
                # Otherwise reset counter and list if the counter is less than four
                counter = 0
                li = []

        if counter >= 4:
            return li[-1],

    def check_three_of_a_kind(self, count):
        """
        Checks for the best THR in a list of cards

        if it's a straight
        :return (tuple): The value of highest card in the flush then the next highest and repeats to the lowest card
        if not
        :return (NoneType): None
        """
        if 3 in count:
            # Finds the position of the three of a kind and get what value it has
            threes_indices = [i for i, x in enumerate(count) if x == 3]
            threes = self.cards[threes_indices]
            # Finds kicker and checks for the highest value
            kicker_indices = [i for i, x in enumerate(count) if x != 3]
            kicker = [self.cards[x] for x in kicker_indices]
            return threes[-1].get_value(), kicker[-1].get_value()

    def check_two_pair(self, count):
        pair_list = [i for i in count if i == 2]  # Create a list where the occurrence of cards is 2
        if len(pair_list) >= 4:  # Checks if there are two or more pairs
            # Finds the position of the pars of a kind and get what value and suit it has
            pair_indices = [i for i, x in enumerate(count) if x == 2]
            pairs = [self.cards[x].get_value() for x in pair_indices]  # Create a lis with the pairs' values
            pairs = sorted(set(pairs), key=pairs.index)  # Make each pair a unique element and sort

            # Get the kicker indices and its value
            kicker_indices = [i for i, x in enumerate(count) if x != 2]
            kicker = [self.cards[x] for x in kicker_indices]
            return pairs[-1], pairs[-2], kicker[-1].get_value()

    def check_pair(self, count):
        pair_list = [i for i in count if i == 2]  # Create a list where the occurrence of cards is 2
        if len(pair_list) == 2:  # Checks if there are two or more pairs
            # Finds the position of the pairs of a kind and get its value
            pair_indices = [i for i, x in enumerate(count) if x == 2]
            pair = [self.cards[x].get_value() for x in pair_indices]

            # Finds the three kickers and their values
            kicker_indices = [i for i, x in enumerate(count) if x != 2]
            kicker = [self.cards[x] for x in kicker_indices]

            return pair[-1], kicker[-1].get_value(), kicker[-2].get_value(), kicker[-3].get_value()

    def its_high_cards(self):
        cards = self.cards
        return cards[-1].get_value(), cards[-2].get_value(), \
            cards[-3].get_value(), cards[-4].get_value(), cards[-5].get_value()

