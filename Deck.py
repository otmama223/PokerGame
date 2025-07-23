#Game Deck

import random
import Card

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Deck():
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        self.shuffle(self)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self, num=1):
        return [self.cards.pop() for i in range(num)]