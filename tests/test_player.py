from blackjack.player import Player
from blackjack.card import Card


player = Player("Card Counter")


def test_create_player():

    assert player.name == "Card Counter"
    assert player.hand == []


def test_receive_card():
    card = Card("A")
    player.receive_card(card)

    assert player.hand[0].card_type == "A"
