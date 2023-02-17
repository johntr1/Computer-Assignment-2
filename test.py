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

