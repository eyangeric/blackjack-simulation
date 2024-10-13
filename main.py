from blackjack.player import Player
from blackjack.dealer import Dealer
from blackjack.shoe import Shoe
from blackjack.deck import Deck
from blackjack.table import Table


num_decks = 2
player_name = 'Card Counter'
dealer_name = 'The Casino'

player = Player(name=player_name)
dealer = Dealer(name=dealer_name)
deck = Deck()
shoe = Shoe(num_decks, deck)
table = Table(dealer, player, shoe)

# start game
table.shoe.shuffle()

table.initial_deal()

for hand in table.player.hands:
    hand_type = table.player.check_initial_hand(hand)
    print(hand_type)

# while len(table.shoe.cards) > 0:
#     table.initial_deal()
#     breakpoint()






