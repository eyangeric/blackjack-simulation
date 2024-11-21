from src.models.dealer import Dealer
from src.models.shoe import Shoe
from src.models.deck import Deck
from src.models.table import Table
from src.models.card_counter import CardCounter


num_decks = 1

card_counter = CardCounter()
dealer = Dealer()
deck = Deck()
shoe = Shoe(num_decks, deck)
table = Table(dealer, card_counter, shoe)

# start game
table.shoe.shuffle()

table.initial_deal()
table.card_counter.check_initial_hand()

# while len(table.shoe.cards) > 0:
#     try:
#         table.initial_deal()
#     except:
#         print("out of cards")
    
