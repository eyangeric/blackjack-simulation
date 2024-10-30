from blackjack.card import Card
from blackjack.hand import Hand
from strategy import *


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hands = [Hand()]

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

    def get_count_type(self) -> str:
        

    # def check_initial_strategy(self, running_count: int, true_count: int):
    #     if self.hand_type == "pair":
    #         pair_split_strategy.get(self.cards[0].card_type).get("deviation")






# class Player:
#     def __init__(self, name: str):
#         self.name = name
#         self.hands = []
#         self.cards = []

#     def receive_initial_hand(self, card: Card):
#         self.cards.append(card)
#         num_cards = len(self.cards)

#         if num_cards == 2:
#             hand = Hand(self.cards[0])
#             hand.receive_card(self.cards[1])
#             self.hands.append(hand)
#             # self.cards.clear()
#             return "Ready to Play!"
#         else:
#             return "Need 1 more card"

#     def check_initial_hand(self, hand: Hand):
#         if hand.cards[0].value == hand.cards[1].value:
#             hand_type = "pair"
#         elif hand.sum_count > 1:
#             if 21 in hand.sums:
#                 hand_type = "black jack"
#             else:
#                 hand_type = "soft"
#         elif hand.sums[0] in (15, 16, 17):
#             hand_type = "surrender"
#         else:
#             hand_type = "hard"
#         self.hand_type = hand_type

#     def check_initial_strategy(self, deviation: str, running_count: int, true_count: int):
#         if self.hand_type == "pair":
#             pair_split_strategy.get(self.cards[0].card_type).get("deviation")


#     def check_deviation(self, deviation: str, running_count: int, true_count: int):
#         deviation_number = int(deviation[:-1])
#         deviation_direction = deviation[-1]
#         if deviation_number == 0:
#             if deviation_direction == "-" and running_count < 0:
#                 deviation_status = "deviate"
#             elif deviation_direction == "+" and running_count > 0:
#                 deviation_status = "deviate"
#             else:
#                 deviation_status = "basic strategy"
#         else:
#             if deviation_direction == "-" and true_count <= deviation_number:
#                 deviation_status = "deviate"
#             elif deviation_direction == "+" and true_count >= deviation_number:
#                 deviation_status = "deviate"
#             else:
#                 deviation_status = "basic strategy"
#         return deviation_status

#     def initial_play(self, hand: Hand, dealer_show_card: int | str, running_count: int, true_count: int):

