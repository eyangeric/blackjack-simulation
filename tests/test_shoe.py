from blackjack.shoe import Shoe
from blackjack.deck import Deck


deck = Deck()
num_decks = 2
shoe = Shoe(num_decks, deck)


def test_number_of_cards():
    assert len(shoe.cards) == 104


def test_deal_card():
    assert shoe.deal_card().card_type in [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        "J",
        "Q",
        "K",
        "A",
    ]

    shoe.cards = []
    assert shoe.deal_card() == "No more cards!"
