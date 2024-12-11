from src.models.hand import Hand
from src.models.card import Card


class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.hand = Hand()

    def play(self):
        while max(self.hand.card_sums) < 17:
            self.hand.add


        while not self.hand.done:
            self.hand.check_21()
            if self.hand.card_sums == [17]:
                self.hand.done = True
                return
            elif 18 in self.hand.card_sums or 19 in self.hand.card_sums or 20 in self.hand.card_sums:
                self.hand.done = True
                return
            self.hand.add_card(card)
            self.hand.check_bust()
