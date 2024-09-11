from blackjack.dealer import Dealer
from blackjack.player import Player
from blackjack.shoe import Shoe
from blackjack.deck import Deck
from blackjack.table import Table


player = Player("Card Counter")
dealer = Dealer("Dealer")
deck = Deck()
num_decks = 2
shoe = Shoe(num_decks, deck)
table = Table(dealer, player, shoe)


def test_initial_deal():
    table.initial_deal()

    assert len(table.player.hand) == 2
    assert len(table.dealer.hand) == 2


def test_initial_true_count():
    table.player.hand == ["A", 10]
    table.dealer.hand == [7, "K"]

    assert table.running_count == -3
    assert table.true_count == int(-3 / 100 / 52)
