from blackjack.card import Card


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def receive_card(self, card: Card):
        return self.hand.append(card)
