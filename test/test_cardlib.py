import pytest
from enum import Enum
from cardlib import *


# This test assumes you call your suit class "Suit" and the suits "Hearts and "Spades"
def test_cards():
    # The following are from the sample test
    h5 = NumberedCard(4, Suit.Hearts)
    assert isinstance(h5.suit, Enum)

    sk = KingCard(Suit.Spades)
    assert sk.get_value() == 13

    assert h5 < sk
    assert h5 == h5

    with pytest.raises(TypeError):
        pc = PlayingCard(Suit.Clubs)

    # The following are additional tests required by the assignment

    cq = QueenCard(Suit.Clubs)
    assert cq.get_value() == 12
    assert cq.suit == Suit.Clubs

    assert cq == cq

    dj = JackCard(Suit.Diamonds)

    assert dj.get_value() == 11
    assert not dj.suit == cq.suit
    assert str(dj) == "Jack of Diamonds"

    d6 = NumberedCard(6, Suit.Diamonds)

    assert d6.suit == dj.suit

    h9 = NumberedCard(9, Suit.Hearts)
    h10 = NumberedCard(10, Suit.Hearts)

    assert h9.get_value() < h10.get_value() and h9.suit == h10.suit

    assert str(h9) == "9 of Hearts"


# This test assumes you call your shuffle method "shuffle" and the method to draw a card "draw"
def test_deck():
    # The following code from this test are from the sample code
    d = StandardDeck()
    c1 = d.draw()
    c2 = d.draw()
    assert not c1 == c2

    d2 = StandardDeck()
    d2.shuffle()
    c3 = d2.draw()
    c4 = d2.draw()
    assert not ((c3, c4) == (c1, c2))

    # The following is additional code required by the assignment

    d3 = StandardDeck()
    assert len(d3.deck) == 52
    assert len(d2.deck) == 50 and len(d.deck) == 50


# This test builds on the assumptions above and assumes you store the cards in the hand in the list "cards",
# and that your sorting method is called "sort" and sorts in increasing order
def test_hand():
    # All the following tests are from the sample tests
    h = Hand()
    assert len(h.cards) == 0
    d = StandardDeck()
    d.shuffle()
    h.add_card(d.draw())
    h.add_card(d.draw())
    h.add_card(d.draw())
    h.add_card(d.draw())
    h.add_card(d.draw())
    assert len(h.cards) == 5

    h.sort()
    for i in range(4):
        assert h.cards[i] < h.cards[i + 1] or h.cards[i] == h.cards[i + 1]

    cards = h.cards.copy()
    h.drop_cards([4, 0, 1])

    assert len(h.cards) == 2
    assert h.cards[0] == cards[2]
    assert h.cards[1] == cards[3]

    # Following tests are own tests made by us

    # Same test but with more cards and different indices
    h2 = Hand()
    h2.add_card(d.draw())
    h2.add_card(d.draw())
    h2.add_card(d.draw())
    h2.add_card(d.draw())
    h2.add_card(d.draw())
    h2.add_card(d.draw())
    h2.add_card(d.draw())
    cards2 = h2.cards.copy()
    h2.drop_cards([4, 5, 2, 6, 1])
    assert len(h2.cards) == 2
    assert h2.cards[0] == cards2[0]
    assert h2.cards[1] == cards2[3]

    # Test with specific cards
    h3 = Hand()
    h3.add_card(NumberedCard(1, Suit.Spades))
    h3.add_card(NumberedCard(2, Suit.Spades))
    h3.add_card(NumberedCard(3, Suit.Spades))
    h3.add_card(NumberedCard(4, Suit.Spades))
    h3.add_card(NumberedCard(5, Suit.Spades))
    # Checks if the cards are in a list
    assert type(h3.cards) == list

    assert len(h3.cards) == 5


# This test builds on the assumptions above. Add your type and data for the commented out tests
# and uncomment them!
def test_pokerhands():
    h1 = Hand()
    h1.add_card(QueenCard(Suit.Diamonds))
    h1.add_card(KingCard(Suit.Hearts))

    h2 = Hand()
    h2.add_card(QueenCard(Suit.Hearts))
    h2.add_card(AceCard(Suit.Hearts))

    cl = [NumberedCard(10, Suit.Diamonds), NumberedCard(9, Suit.Diamonds),
          NumberedCard(8, Suit.Clubs), NumberedCard(6, Suit.Spades)]

    ph1 = h1.best_poker_hand(cl)
    assert isinstance(ph1, PokerHand)
    ph2 = h2.best_poker_hand(cl)

    # Checks if the class HandType is an enum
    assert issubclass(HandType, Enum)

    # Checks if the hand type is of the correct one
    assert HandType(ph1.check_poker_hand_value()[0]) == HandType.HIGH_CARD
    # Checks if the hand type's rank values are in correct order according to Poker rules
    assert ph1.check_poker_hand_value() == (1, 13, 12, 10, 9, 8)

    # Check if ph2 is of correct hand type
    assert HandType(ph2.check_poker_hand_value()[0]) == HandType.HIGH_CARD

    # Checks if its rank's values are in correct order
    assert ph2.check_poker_hand_value() == (1, 14, 12, 10, 9, 8)

    assert ph1 < ph2

    cl.pop(0)
    cl.append(QueenCard(Suit.Spades))
    ph3 = h1.best_poker_hand(cl)
    ph4 = h2.best_poker_hand(cl)
    assert ph3 < ph4
    assert ph1 < ph2

    # Checks if the poker hand has the correct values in its tuple
    assert ph3.check_poker_hand_value() == (2, 12, 13, 9, 8)

    # Checks if the hand type is pair
    assert HandType(ph3.check_poker_hand_value()[0]) == HandType.PAIR

    # Same controls for ph4
    assert ph4.check_poker_hand_value() == (2, 12, 14, 9, 8)
    assert HandType(ph4.check_poker_hand_value()[0]) == HandType.PAIR

    cl = [QueenCard(Suit.Clubs), QueenCard(Suit.Spades), KingCard(Suit.Clubs), KingCard(Suit.Spades)]
    ph5 = h1.best_poker_hand(cl)

    # Checks if the hand type is correct and its values
    assert HandType(ph5.check_poker_hand_value()[0]) == HandType.FULL_HOUSE
    assert ph5.check_poker_hand_value() == (7, 13, 12)

    # We have now controlled for same type of hands comparison and a few hand types.
    # Now we test the rest of the hand types to ensure everything is working

    # Test if STRAIGHT_FLUSH works

    h3 = Hand()
    h3.add_card(AceCard(Suit.Diamonds))
    h3.add_card(KingCard(Suit.Diamonds))

    cl = [QueenCard(Suit.Diamonds), JackCard(Suit.Diamonds), NumberedCard(10, Suit.Diamonds), KingCard(Suit.Spades)]

    ph6 = h3.best_poker_hand(cl)
    assert HandType(ph6.check_poker_hand_value()[0]) == HandType.STRAIGHT_FLUSH
    assert ph6.check_poker_hand_value() == (9, 14)

    # Tests for flush
    cl.pop(0)
    cl.append(NumberedCard(5, Suit.Diamonds))

    ph_flush = h3.best_poker_hand(cl)
    assert HandType(ph_flush.check_poker_hand_value()[0]) == HandType.FLUSH
    assert ph_flush.check_poker_hand_value() == (6, 14, 13, 11, 10, 5)

    # Checks for straight flush if the lower ace works
    h4 = Hand()
    h4.add_card(AceCard(Suit.Diamonds))
    h4.add_card(NumberedCard(2, Suit.Diamonds))

    cl = [NumberedCard(3, Suit.Diamonds), NumberedCard(4, Suit.Diamonds), NumberedCard(5, Suit.Diamonds),
          KingCard(Suit.Spades)]
    ph7 = h4.best_poker_hand(cl)

    assert HandType(ph7.check_poker_hand_value()[0]) == HandType.STRAIGHT_FLUSH
    assert ph7.check_poker_hand_value() == (9, 5)

    assert ph7 < ph6

    # Test for straight
    cl.pop(0)
    cl.append(NumberedCard(3, Suit.Spades))

    # Test for straight where AceCard has the value of 1
    ph7 = h4.best_poker_hand(cl)
    assert HandType(ph7.check_poker_hand_value()[0]) == HandType.STRAIGHT
    assert ph7.check_poker_hand_value() == (5, 5)

    # Test for when Ace has value of 14:

    cl = [QueenCard(Suit.Spades), JackCard(Suit.Diamonds), NumberedCard(10, Suit.Diamonds), KingCard(Suit.Spades)]
    ph8 = h3.best_poker_hand(cl)

    assert HandType(ph8.check_poker_hand_value()[0]) == HandType.STRAIGHT
    assert ph8.check_poker_hand_value() == (5, 14)

    # Tests for four of a kind

    h5 = Hand()
    h5.add_card(NumberedCard(7, Suit.Spades))
    h5.add_card(NumberedCard(7, Suit.Diamonds))

    cl = [NumberedCard(7, Suit.Hearts), NumberedCard(7, Suit.Clubs), KingCard(Suit.Spades), NumberedCard(3, Suit.Spades),
          NumberedCard(4, Suit.Hearts)]

    ph9 = h5.best_poker_hand(cl)
    assert HandType(ph9.check_poker_hand_value()[0]) == HandType.FOUR_OF_A_KIND
    assert ph9.check_poker_hand_value() == (8, 7, 13)

    # Tests for three of a kind
    cl.pop(0)
    cl.append(JackCard(Suit.Spades))

    ph9 = h5.best_poker_hand(cl)
    assert HandType(ph9.check_poker_hand_value()[0]) == HandType.THREE_OF_A_KIND
    assert ph9.check_poker_hand_value() == (4, 7, 13)





