from blackjack.deck import Deck


class Shoe:
    def __init__(self, num_decks: int, deck: Deck):
        self.cards = num_decks*deck.cards

    def shuffle(self):
        import random
        random.shuffle(self.cards)