from src.models.dealer import Dealer
from src.models.card import Card


dealer = Dealer("Dealer")


def test_create_dealer():
    assert dealer.name == "Dealer"
    assert dealer.hand == []


def test_receive_card():
    card = Card("A")
    dealer.receive_card(card)

    assert dealer.hand[0].card_type == "A"
