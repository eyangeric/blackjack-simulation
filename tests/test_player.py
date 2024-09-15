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


def test_check_deviation():
    player = Player("Card Counter")

    negative_running_count = -2
    negative_true_count = -1
    negative_running_count_deviation = "0-"
    negative_true_count_deviation = "-1-"
    negative_running_count_action = player.check_deviation(negative_running_count_deviation, negative_running_count, negative_true_count)
    negative_true_count_action = player.check_deviation(negative_true_count_deviation, negative_running_count, negative_true_count)
    assert negative_running_count_action == "deviate"
    assert negative_true_count_action == "deviate"

    positive_running_count = 2
    positive_true_count = 1
    positive_running_count_deviation = "0+"
    positive_true_count_deviation = "-1+"
    high_positive_true_count_deviation = "6+"
    positive_running_count_action = player.check_deviation(positive_running_count_deviation, positive_running_count, positive_true_count)
    positive_true_count_action = player.check_deviation(positive_true_count_deviation, positive_running_count, positive_true_count)    
    assert positive_running_count_action == "deviate"
    assert positive_true_count_action == "deviate"

    basic_strategy_1 = player.check_deviation(negative_running_count_deviation, positive_running_count, positive_true_count)
    basic_strategy_2 = player.check_deviation(negative_true_count_deviation, positive_running_count, positive_true_count)
    basic_strategy_3 = player.check_deviation(positive_running_count_deviation, negative_running_count, negative_true_count)
    basic_strategy_4 = player.check_deviation(high_positive_true_count_deviation, negative_running_count, negative_true_count)
    assert basic_strategy_1 == "basic strategy"
    assert basic_strategy_2 == "basic strategy"
    assert basic_strategy_3 == "basic strategy"
    assert basic_strategy_4 == "basic strategy"
