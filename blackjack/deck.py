from blackjack.card import Card


class Deck:
    card_types = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = 4 * [Card(card_type) for card_type in self.card_types]
