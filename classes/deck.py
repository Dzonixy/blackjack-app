import random
from .card import Card


class Deck:
    def __init__(self):
        self.cards = [Card(suit, number) for suit in ["Spades", "Clubs", "Hearts",
                                                      "Diamonds"] for number in ["A", "2", "3", "4", "5", "6",
                                                                                 "7", "8", "9", "10", "J", "Q", "K"]]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)
