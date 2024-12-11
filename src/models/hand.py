from src.models.card import Card


class Hand:
    def __init__(self):
        self.cards = []
        self.card_sums = [0]

    def add_card(self, card: Card):
        self.cards.append(card)
        self.update_card_sums(card)

    def update_card_sums(self, card: Card):
        new_sums = [
            sum_value + value
            for sum_value in self.card_sums
            for value in card.value
        ]
        self.card_sums = [new_sum for new_sum in new_sums if new_sum < 22]
    
    def check_21(self):
        if len(self.cards) == 2 and 21 in self.card_sums:
            self.black_jack = True
            self.done = True
            return "Black Jack!"
        elif 21 in self.card_sums:
            self.play_status = "stay"
            self.final_value = 21
            self.done = True
            return "21!"

    def check_bust(self):
        if not self.card_sums:
            self.bust = True
            self.done = True
            return

    def get_final_value(self):
        self.final_value = max(self.card_sums)

    def card_counter_bet_amount(self, bet_amount: int):
        self.bet_amount = bet_amount
