from src.models.card import Card


class Deck:
    def __init__(self):
        self.cards = 4 * [Card(card_type) for card_type in Card.card_types]
