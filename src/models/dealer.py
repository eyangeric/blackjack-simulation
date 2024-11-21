from src.models.hand import Hand
from src.models.card import Card


class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.hand = Hand()
        self.card_sums = [0]
        self.status = "play"

    def receive_initial_hand(self, card: Card):
        self.hand.add_card(card)

    def receive_card(self, card: Card):
        action = self.check_action()
        if action == "hit":
            self.hand.add_card(card)

    def update_card_sums(self, incoming_card_values):
        new_sums = [
            sum_value + value
            for sum_value in self.card_sums
            for value in incoming_card_values
        ]
        self.card_sums = [new_sum for new_sum in new_sums if new_sum < 22]

    def check_action(self):
        action = "hit"
        if 21 in self.card_sums:
            action = "black jack"
        elif self.card_sums == [17]:
            action = "stay"
        elif 18 in self.card_sums or 19 in self.card_sums or 20 in self.card_sums:
            action = "stay"
        return action

    def check_status(self):
        if len(self.card_sums) == 1 and self.card_sums[0] > 21:
            self.status = "bust"
