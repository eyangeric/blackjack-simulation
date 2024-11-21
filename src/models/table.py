from src.models.dealer import Dealer
from src.models.card_counter import CardCounter
from src.models.shoe import Shoe


class Table:
    def __init__(self, dealer: Dealer, card_counter: CardCounter, shoe: Shoe):
        self.dealer = dealer
        self.card_counter = card_counter
        self.shoe = shoe
        self.running_count = 0
        self.true_count = 0

    def calculate_true_count(self):
        self.true_count = int(self.running_count / len(self.shoe.cards) / 52)

    def initial_deal_count(self):
        card_counter_count = sum([card.count_value for card in self.card_counter.hands[0].cards])
        self.running_count += card_counter_count
        self.running_count += self.dealer.hand.cards[1].count_value

    def initial_deal(self):
        self.card_counter.receive_initial_hand(self.shoe.deal_card())
        self.dealer.receive_initial_hand(self.shoe.deal_card())
        self.card_counter.receive_initial_hand(self.shoe.deal_card())
        self.dealer.receive_initial_hand(self.shoe.deal_card())
        self.initial_deal_count()
        self.calculate_true_count()
