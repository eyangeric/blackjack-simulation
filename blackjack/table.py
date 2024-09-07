from blackjack.dealer import Dealer
from blackjack.player import Player
from blackjack.shoe import Shoe
from blackjack.discard_tray import DiscardTray


class Table:
    def __init__(
        self, dealer: Dealer, player: Player, shoe: Shoe, discard_tray: DiscardTray
    ):
        self.dealer = dealer
        self.player = player
        self.shoe = shoe
        self.discard_tray = discard_tray
        self.running_count = 0


    def initial_deal_count(self):
        player_count = sum([card.count_value for card in self.player.hand])
        self.running_count += player_count
        self.running_count += self.dealer.hand[1].count_value

    def initial_deal(self):
        self.player.receive_card(self.shoe.deal_card())
        self.dealer.receive_card(self.shoe.deal_card())
        self.player.receive_card(self.shoe.deal_card())
        self.dealer.receive_card(self.shoe.deal_card())
        self.initial_deal_count()

