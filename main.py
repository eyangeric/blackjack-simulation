from blackjack.player import Player
from blackjack.dealer import Dealer
from blackjack.shoe import Shoe
from blackjack.deck import Deck
from blackjack.discard_tray import DiscardTray
from blackjack.table import Table


num_decks = 2
player_name = 'Card Counter'
dealer_name = 'The Casino'

player = Player(name=player_name)
dealer = Dealer(name=dealer_name)
deck = Deck()
shoe = Shoe(num_decks, deck)
discard_tray = DiscardTray()
table = Table(dealer, player, shoe, discard_tray)

# start game
table.shoe.shuffle()

while len(table.shoe.cards) > 0:
    table.initial_deal()
    breakpoint()






