from enum import Enum


# class syntax
class Suit(Enum):
    Hearts = 4
    Spades = 3
    Clubs = 2
    Diamonds = 1

    def __str__(self):
        return self.name

# functional syntax
print(type(Suit.Hearts))





for i in Suit:
    print(i)



 for card in reversed(cards):
    for k in range(1, 5):
        if (card.get_value() - k, card.suit) not in cards:
            break
        straight_flush = True
        if straight_flush:
            return card.get_value(), card.suit


                cards = [(card.get_value(), c.suit) for card in cards]
                ace_cards = [(1, c.suit) for c in self.cards if c.get_value() == 14]

                cards = ace_cards + self.cards
                print(cards)
                cards = list(reversed(cards))
                print(cards)
                for i, card in enumerate(cards):
                    for k in range(1, 5):
                        if (card.get_value - k, card.suit) not in cards:
                            break
                    straight_flush = True
                    if straight_flush:
                        return card.get_value(), card.suit









