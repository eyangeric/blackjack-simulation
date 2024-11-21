from src.models.card import Card


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)


# class Hand:
#     def __init__(self, card: Card):
#         self.cards = [card]
#         self.sum_count = 1

#         if card.card_type == "A":
#             self.sums = card.value
#             self.sum_count += 1
#         else:
#             self.sums = [card.value]

#     def receive_card(self, card: Card):
#         self.cards.append(card)
#         if card.card_type == "A":
#             if self.sum_count > 1:
#                 self.sums = [value + min(card.value) for value in self.sums]
#             else:
#                 self.sum_count += 1
#                 self.sums = [value + self.sums[0] for value in card.value]
#         else:
#             self.sums = [value + card.value for value in self.sums]
