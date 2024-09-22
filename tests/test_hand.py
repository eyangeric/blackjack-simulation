from blackjack.card import Card
from blackjack.hand import Hand


card_A = Card("A")
card_2 = Card(2)

def test_hand_first_card_A():
    hand = Hand(card_A)
    assert hand.sum_count == 2
    assert hand.sums == card_A.value

def test_hand_first_card_2():
    hand = Hand(card_2)
    assert hand.sum_count == 1
    assert hand.sums == [card_2.value]

def test_receive_card_first_card_A():
    hand_first_card_A = Hand(card_A)
    hand_first_card_A.receive_card(card_A)
    assert hand_first_card_A.sum_count == 2
    assert hand_first_card_A.sums == [2, 12]

    hand_first_card_A.receive_card(card_2)
    assert hand_first_card_A.sum_count == 2
    assert hand_first_card_A.sums == [4, 14]

def test_receive_card_first_card_2():
    hand_first_card_2 = Hand(card_2)
    hand_first_card_2.receive_card(card_2)
    assert hand_first_card_2.sum_count == 1
    assert hand_first_card_2.sums == [4]

    hand_first_card_2.receive_card(card_A)
    assert hand_first_card_2.sum_count == 2
    assert hand_first_card_2.sums == [5, 15]
