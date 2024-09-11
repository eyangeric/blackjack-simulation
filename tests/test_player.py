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


def test_check_initial_hand_pair():
    card_4 = Card(4)
    player = Player("Card Counter")
    player.receive_card(card_4)
    player.receive_card(card_4)
    player.check_initial_hand()
    assert player.hand_type == "pair"


def test_check_initial_hand_soft():
    card_4 = Card(4)
    card_A = Card("A")
    player = Player("Card Counter")
    player.receive_card(card_4)
    player.receive_card(card_A)
    player.check_initial_hand()
    assert player.hand_type == "soft"


def test_check_initial_hand_hard():
    card_4 = Card(4)
    card_5 = Card(5)
    player = Player("Card Counter")
    player.receive_card(card_4)
    player.receive_card(card_5)
    player.check_initial_hand()
    assert player.hand_type == "hard"
