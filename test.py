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


 cards
 for card in reversed(cards):
            for k in range(1, 5):
                if (card.get_value() - k, card.suit) not in cards:
                    break
            straight_flush = True
            if straight_flush:
                return card.get_value(), card.suit














