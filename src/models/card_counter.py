from src.models.card import Card
from src.models.hand import Hand
from strategy import *


class CardCounter:
    def __init__(self):
        self.name = "Card Counter"
        self.hands = [Hand()]

    def receive_initial_hand(self, card: Card):
        self.hands[0].add_card(card)

    def receive_card(self, card: Card, hand_index=0):
        self.hands[hand_index].add_card(card)

    def check_initial_hand(self):
        card_values = [card.value[0] for card in self.hands[0].cards]
        card_types = [card.card_type for card in self.hands[0].cards]
        if card_values[0] == card_values[1]:
            hand_type = "pair"
        elif "A" in card_types:
            if 10 in card_values:
                hand_type = "black jack"
            else:
                hand_type = "soft"
        elif sum(card_values) in (15, 16, 17):
            hand_type = "surrender"
        else:
            hand_type = "hard"
        self.hand_type = hand_type

    def deviation_count_type(self, deviation: str) -> str:
        if deviation[0] == "0":
            count_type = "running count"
        else:
            count_type = "true count"
        return count_type

    def check_deviation(self, deviation: str, true_count: int, running_count: int):
        count_type = self.deviation_count_type(deviation)
        deviation_num = int(deviation[:-1])
        deviation_direction = deviation[-1]

        # Determine which count to use
        count = true_count if count_type == "true count" else running_count

        # Determine whether to deviate based on the direction
        if (deviation_direction == "+" and count >= deviation_num) or (
            deviation_direction == "-" and count <= deviation_num
        ):
            return "deviation"

        return "basic"