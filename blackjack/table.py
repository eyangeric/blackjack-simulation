from blackjack.dealer import Dealer
from blackjack.player import Player
from blackjack.shoe import Shoe


class Table:
    def __init__(self, dealer: Dealer, player: Player, shoe: Shoe):
        self.dealer = dealer
        self.player = player
        self.shoe = shoe
        self.running_count = 0
        self.true_count = 0

    def calculate_true_count(self):
        self.true_count = int(self.running_count / len(self.shoe.cards) / 52)

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
        self.calculate_true_count()
