from blackjack.card import Card


class Player:
    strategy = {
        "pair": {
            "split": {
                "A": [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
                9: [2, 3, 4, 5, 6, 8, 9],
                8: [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
                7: [2, 3, 4, 5, 6, 7],
                6: [2, 3, 4, 5, 6],
                4: [5, 6],
                3: [2, 3, 4, 5, 6, 7],
                2: [2, 3, 4, 5, 6, 7],
            },
            "deviation": {
                10: {
                    4: "6+",
                    5: "5+",
                    6: "4+",
                }
            },
        },
        "soft": {
            "double": {
                8: [6],
                7: [2, 3, 4, 5, 6],
                6: [3, 4, 5, 6],
                5: [4, 5, 6],
                4: [4, 5, 6],
                3: [5, 6],
                2: [5, 6],
            },
            "hit": {7: [9, 10, "A"], 6: [7, 8, 9, 10, "A"]},
        },
    }

    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def receive_card(self, card: Card):
        return self.hand.append(card)

    def check_initial_hand(self):
        card_values = [card.value for card in self.hand]
        card_types = [card.card_type for card in self.hand]

        if card_values[0] == card_values[1]:
            hand_type = "pair"
        elif "A" in card_types:
            hand_type = "soft"
        else:
            hand_type = "hard"
        self.hand_type = hand_type

    def check_deviation(self, deviation: str, running_count: int, true_count: int):
        deviation_number = int(deviation[:-1])
        deviation_direction = deviation[-1]
        if deviation_number == 0:
            if deviation_direction == "-" and running_count < 0:
                deviation_status = "deviate"
            elif deviation_direction == "+" and running_count > 0:
                deviation_status = "deviate"
            else:
                deviation_status = "basic strategy"
        else:
            if deviation_direction == "-" and true_count <= deviation_number:
                deviation_status = "deviate"
            elif deviation_direction == "+" and true_count >= deviation_number:
                deviation_status = "deviate"
            else:
                deviation_status = "basic strategy"
        return deviation_status
        

    # def play(self, dealer_show_card: int | str, running_count: int, true_count: int):
    #     if len(self.hand) == 2:
    #         if self.check_initial_hand() == "pair":
    #             if self.hand[0].card_type in list(self.strategy["pair"]["deviation"].keys()):
    #                 if dealer_show_card in list(self.strategy["pair"]["deviation"][self.hand[0].card_type].keys()):


                
