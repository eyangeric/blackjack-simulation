from src.models.deck import Deck


def test_number_of_cards():
    deck = Deck()

    assert len(deck.cards) == 52
    assert len([card.card_type for card in deck.cards if card.card_type == "A"]) == 4
