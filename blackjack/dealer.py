from blackjack.card import Card


class Dealer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_card(self, card: Card):
        return self.hand.append(card)
