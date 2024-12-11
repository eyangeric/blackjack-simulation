from src.models.dealer import Dealer
from src.models.card_counter import CardCounter
from src.models.shoe import Shoe


class Table:
    def __init__(self, dealer: Dealer, card_counter: CardCounter, shoe: Shoe, minimum_bet_amount: int):
        self.dealer = dealer
        self.card_counter = card_counter
        self.shoe = shoe
        self.minimum_bet_amount = minimum_bet_amount

    def calculate_true_count(self):
        self.shoe.true_count = int(self.running_count / len(self.shoe.cards) / 52)

    def initial_deal_count(self):
        card_counter_count = sum([card.count_value for card in self.card_counter.hands[0].cards])
        self.shoe.running_count += card_counter_count
        self.shoe.running_count += self.dealer.hand.cards[1].count_value

    def initial_deal(self):
        self.card_counter.hands[0].add_card(self.shoe.deal_card())
        self.dealer.hand.add_card(self.shoe.deal_card())
        self.card_counter.hands[0].add_card(self.shoe.deal_card())
        self.dealer.hand.add_card(self.shoe.deal_card())
        self.initial_deal_count()
        self.calculate_true_count()

    # def card_counter_play_action(self):
    #     for i, card_counter_hand in enumerate(self.card_counter.hands):
    #         if self.card_counter.play_decision == "stay":
    #             card_counter_hand.play_status = "done"
    #             return
    #         elif self.card_counter.play_decision == "hit":
    #             self.card_counter.receive_card(self.shoe.deal_card(), hand_index=i)
    #         elif self.card_counter.play_decision == "double":
    #             self.card_counter.receive_card(self.shoe.deal_card(), hand_index=i)
    #             card_counter_hand.play_status = "done"
    #             return
    #         elif self.card_counter.play_decision == "surrender":
    #             card_counter_hand.play_status = "surrender"
    #         elif self.card_counter.play_decision == "play":

# hand class can hold the play status of the hand (done, surrender)
# hand class also hold win status




