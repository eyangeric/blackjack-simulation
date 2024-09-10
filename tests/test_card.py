from blackjack.card import Card


def test_int_card():
    card_2 = Card(2)
    card_10 = Card(10)

    assert card_2.value == 2
    assert card_10.value == 10
    assert card_2.count_value == 1
    assert card_10.count_value == -1

def test_str_card():
    card_K = Card("K")
    card_A = Card("A")

    assert card_K.value == 10
    assert card_A.value == (1, 11)
    assert card_K.count_value == -1
    assert card_A.count_value == -1
