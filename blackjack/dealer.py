from blackjack.hand import Hand


class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.hand = Hand()

    def receive_card(self, card):
        self.hand.add_card(card)







# class Dealer:
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
#             return "Ready to Play!"
#         else:
#             return "Need 1 more card"
