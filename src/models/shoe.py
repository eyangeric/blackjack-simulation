import random

from src.models.deck import Deck
from src.models.card import Card


class Shoe:
    def __init__(self, num_decks: int, deck: Deck):
        self.cards = num_decks * deck.cards
        self.running_count = 0
        self.true_count = 0

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None

    def add_running_count(self, card: Card):
        self.running_count += card.assign_count_value

    def calculate_true_count(self):
        self.true_count += self.running_count / len(self.cards) / 52

    def deal_initial(self, player, dealer):
        for i in range(2):
            player_card = self.deal_card()
            player.receive_card(player_card)
            dealer_card = self.deal_card()
            dealer.receive_card(dealer_card)
            if i == 1:
                self.add_running_count(player_card)
                self.add_running_count(dealer)
            else:
                self.add_running_count(player_card)
        self.calculate_true_count()

    def __repr__(self):
        return f"Shoe({len(self.cards)} cards remaining)"
