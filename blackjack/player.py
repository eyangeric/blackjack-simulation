from blackjack.card import Card


class Player:
    pair_split_strategy = {
        "A": {
            2: {
                "basic": "split"
            },
            3: {
                "basic": "split"
            },
            4: {
                "basic": "split"
            },
            5: {
                "basic": "split"
            },
            6: {
                "basic": "split"
            },
            7: {
                "basic": "split"
            },
            8: {
                "basic": "split"
            },
            9: {
                "basic": "split"
            },
            10: {
                "basic": "split"
            },
            "J": {
                "basic": "split"
            },
            "Q": {
                "basic": "split"
            },
            "K": {
                "basic": "split"
            },
            "A": {
                "basic": "split"
            },
        },
        "K": {
            2: {
                "basic": "play"
            },
            3: {
                "basic": "play"
            },
            4: {
                "basic": "play",
                "deviation": ("6+", "split")
            },
            5: {
                "basic": "play",
                "deviation": ("5+", "split")
            },
            6: {
                "basic": "play",
                "deviation": ("4+", "split")
            },
            7: {
                "basic": "play"
            },
            8: {
                "basic": "play"
            },
            9: {
                "basic": "play"
            },
            10: {
                "basic": "play"
            },
            "J": {
                "basic": "play"
            },
            "Q": {
                "basic": "play"
            },
            "K": {
                "basic": "play"
            },
            "A": {
                "basic": "play"
            },
        },
        "Q": {
            2: {
                "basic": "play"
            },
            3: {
                "basic": "play"
            },
            4: {
                "basic": "play",
                "deviation": ("6+", "split")
            },
            5: {
                "basic": "play",
                "deviation": ("5+", "split")
            },
            6: {
                "basic": "play",
                "deviation": ("4+", "split")
            },
            7: {
                "basic": "play"
            },
            8: {
                "basic": "play"
            },
            9: {
                "basic": "play"
            },
            10: {
                "basic": "play"
            },
            "J": {
                "basic": "play"
            },
            "Q": {
                "basic": "play"
            },
            "K": {
                "basic": "play"
            },
            "A": {
                "basic": "play"
            },
        },
        "J": {
            2: {
                "basic": "play"
            },
            3: {
                "basic": "play"
            },
            4: {
                "basic": "play",
                "deviation": ("6+", "split")
            },
            5: {
                "basic": "play",
                "deviation": ("5+", "split")
            },
            6: {
                "basic": "play",
                "deviation": ("4+", "split")
            },
            7: {
                "basic": "play"
            },
            8: {
                "basic": "play"
            },
            9: {
                "basic": "play"
            },
            10: {
                "basic": "play"
            },
            "J": {
                "basic": "play"
            },
            "Q": {
                "basic": "play"
            },
            "K": {
                "basic": "play"
            },
            "A": {
                "basic": "play"
            },
        },
        10: {
            2: {
                "basic": "play"
            },
            3: {
                "basic": "play"
            },
            4: {
                "basic": "play",
                "deviation": ("6+", "split")
            },
            5: {
                "basic": "play",
                "deviation": ("5+", "split")
            },
            6: {
                "basic": "play",
                "deviation": ("4+", "split")
            },
            7: {
                "basic": "play"
            },
            8: {
                "basic": "play"
            },
            9: {
                "basic": "play"
            },
            10: {
                "basic": "play"
            },
            "J": {
                "basic": "play"
            },
            "Q": {
                "basic": "play"
            },
            "K": {
                "basic": "play"
            },
            "A": {
                "basic": "play"
            },
        },
        9: {
            2: {
                "basic": "split"
            },
            3: {
                "basic": "split"
            },
            4: {
                "basic": "split"
            },
            5: {
                "basic": "split"
            },
            6: {
                "basic": "split"
            },
            7: {
                "basic": "play"
            },
            8: {
                "basic": "split"
            },
            9: {
                "basic": "split"
            },
            10: {
                "basic": "play"
            },
            "J": {
                "basic": "play"
            },
            "Q": {
                "basic": "play"
            },
            "K": {
                "basic": "play"
            },
            "A": {
                "basic": "play"
            },
        },
        8: {
            2: {
                "basic": "split"
            },
            3: {
                "basic": "split"
            },
            4: {
                "basic": "split"
            },
            5: {
                "basic": "split"
            },
            6: {
                "basic": "split"
            },
            7: {
                "basic": "split"
            },
            8: {
                "basic": "split"
            },
            9: {
                "basic": "split"
            },
            10: {
                "basic": "split"
            },
            "J": {
                "basic": "split"
            },
            "Q": {
                "basic": "split"
            },
            "K": {
                "basic": "split"
            },
            "A": {
                "basic": "split"
            },
        },
        7: {
            2: {
                "basic": "split"
            },
            3: {
                "basic": "split"
            },
            4: {
                "basic": "split"
            },
            5: {
                "basic": "split"
            },
            6: {
                "basic": "split"
            },
            7: {
                "basic": "split"
            },
            8: {
                "basic": "play"
            },
            9: {
                "basic": "play"
            },
            10: {
                "basic": "play"
            },
            "J": {
                "basic": "play"
            },
            "Q": {
                "basic": "play"
            },
            "K": {
                "basic": "play"
            },
            "A": {
                "basic": "play"
            },
        },
        6: {
            2: {
                "basic": "split"
            },
            3: {
                "basic": "split"
            },
            4: {
                "basic": "split"
            },
            5: {
                "basic": "split"
            },
            6: {
                "basic": "split"
            },
            7: {
                "basic": "play"
            },
            8: {
                "basic": "play"
            },
            9: {
                "basic": "play"
            },
            10: {
                "basic": "play"
            },
            "J": {
                "basic": "play"
            },
            "Q": {
                "basic": "play"
            },
            "K": {
                "basic": "play"
            },
            "A": {
                "basic": "play"
            },
        },
        5: {
            2: {
                "basic": "play"
            },
            3: {
                "basic": "play"
            },
            4: {
                "basic": "play"
            },
            5: {
                "basic": "play"
            },
            6: {
                "basic": "play"
            },
            7: {
                "basic": "play"
            },
            8: {
                "basic": "play"
            },
            9: {
                "basic": "play"
            },
            10: {
                "basic": "play"
            },
            "J": {
                "basic": "play"
            },
            "Q": {
                "basic": "play"
            },
            "K": {
                "basic": "play"
            },
            "A": {
                "basic": "play"
            },
        },
        5: {
            2: {
                "basic": "play"
            },
            3: {
                "basic": "play"
            },
            4: {
                "basic": "play"
            },
            5: {
                "basic": "split"
            },
            6: {
                "basic": "split"
            },
            7: {
                "basic": "play"
            },
            8: {
                "basic": "play"
            },
            9: {
                "basic": "play"
            },
            10: {
                "basic": "play"
            },
            "J": {
                "basic": "play"
            },
            "Q": {
                "basic": "play"
            },
            "K": {
                "basic": "play"
            },
            "A": {
                "basic": "play"
            },
        },
        3: {
            2: {
                "basic": "split"
            },
            3: {
                "basic": "split"
            },
            4: {
                "basic": "split"
            },
            5: {
                "basic": "split"
            },
            6: {
                "basic": "split"
            },
            7: {
                "basic": "split"
            },
            8: {
                "basic": "play"
            },
            9: {
                "basic": "play"
            },
            10: {
                "basic": "play"
            },
            "J": {
                "basic": "play"
            },
            "Q": {
                "basic": "play"
            },
            "K": {
                "basic": "play"
            },
            "A": {
                "basic": "play"
            },
        },
        2: {
            2: {
                "basic": "split"
            },
            3: {
                "basic": "split"
            },
            4: {
                "basic": "split"
            },
            5: {
                "basic": "split"
            },
            6: {
                "basic": "split"
            },
            7: {
                "basic": "split"
            },
            8: {
                "basic": "play"
            },
            9: {
                "basic": "play"
            },
            10: {
                "basic": "play"
            },
            "J": {
                "basic": "play"
            },
            "Q": {
                "basic": "play"
            },
            "K": {
                "basic": "play"
            },
            "A": {
                "basic": "play"
            },
        },
    }

    soft_strategy = {
        9: {
            2: {
                "basic": "stay",
            },
            3: {
                "basic": "stay",
            },
            4: {
                "basic": "stay",
            },
            5: {
                "basic": "stay",
            },
            6: {
                "basic": "stay",
            },
            7: {
                "basic": "stay",
            },
            8: {
                "basic": "stay",
            },
            9: {
                "basic": "stay",
            },
            10: {
                "basic": "stay",
            },
            "J": {
                "basic": "stay",
            },
            "Q": {
                "basic": "stay",
            },
            "K": {
                "basic": "stay",
            },
            "A": {
                "basic": "stay",
            },
        },
        8: {
            2: {
                "basic": "stay",
            },
            3: {
                "basic": "stay",
            },
            4: {
                "basic": "stay",
                "deviation": ("3+", "double"),
            },
            5: {
                "basic": "stay",
                "deviation": ("1+", "double"),
            },
            6: {
                "basic": "double",
                "deviation": ("0-", "stay"),
            },
            7: {
                "basic": "stay",
            },
            8: {
                "basic": "stay",
            },
            9: {
                "basic": "stay",
            },
            10: {
                "basic": "stay",
            },
            "J": {
                "basic": "stay",
            },
            "Q": {
                "basic": "stay",
            },
            "K": {
                "basic": "stay",
            },
            "A": {
                "basic": "stay",
            },
        },
        7: {
            2: {
                "basic": "double",
            },
            3: {
                "basic": "double",
            },
            4: {
                "basic": "double",
            },
            5: {
                "basic": "double",
            },
            6: {
                "basic": "double",
            },
            7: {
                "basic": "stay",
            },
            8: {
                "basic": "stay",
            },
            9: {
                "basic": "hit",
            },
            10: {
                "basic": "hit",
            },
            "J": {
                "basic": "hit",
            },
            "Q": {
                "basic": "hit",
            },
            "K": {
                "basic": "hit",
            },
            "A": {
                "basic": "hit",
            },
        },
        6: {
            2: {
                "basic": "stay",
                "deviation": ("1+", "double")
            },
            3: {
                "basic": "double",
            },
            4: {
                "basic": "double",
            },
            5: {
                "basic": "double",
            },
            6: {
                "basic": "double",
            },
            7: {
                "basic": "hit",
            },
            8: {
                "basic": "hit",
            },
            9: {
                "basic": "hit",
            },
            10: {
                "basic": "hit",
            },
            "J": {
                "basic": "hit",
            },
            "Q": {
                "basic": "hit",
            },
            "K": {
                "basic": "hit",
            },
            "A": {
                "basic": "hit",
            },
        },
        5: {
            2: {
                "basic": "stay",
            },
            3: {
                "basic": "stay",
            },
            4: {
                "basic": "double",
            },
            5: {
                "basic": "double",
            },
            6: {
                "basic": "double",
            },
            7: {
                "basic": "hit",
            },
            8: {
                "basic": "hit",
            },
            9: {
                "basic": "hit",
            },
            10: {
                "basic": "hit",
            },
            "J": {
                "basic": "hit",
            },
            "Q": {
                "basic": "hit",
            },
            "K": {
                "basic": "hit",
            },
            "A": {
                "basic": "hit",
            },
        },
        4: {
            2: {
                "basic": "stay",
            },
            3: {
                "basic": "stay",
            },
            4: {
                "basic": "double",
            },
            5: {
                "basic": "double",
            },
            6: {
                "basic": "double",
            },
            7: {
                "basic": "hit",
            },
            8: {
                "basic": "hit",
            },
            9: {
                "basic": "hit",
            },
            10: {
                "basic": "hit",
            },
            "J": {
                "basic": "hit",
            },
            "Q": {
                "basic": "hit",
            },
            "K": {
                "basic": "hit",
            },
            "A": {
                "basic": "hit",
            },
        },
        3: {
            2: {
                "basic": "stay",
            },
            3: {
                "basic": "stay",
            },
            4: {
                "basic": "stay",
            },
            5: {
                "basic": "double",
            },
            6: {
                "basic": "double",
            },
            7: {
                "basic": "hit",
            },
            8: {
                "basic": "hit",
            },
            9: {
                "basic": "hit",
            },
            10: {
                "basic": "hit",
            },
            "J": {
                "basic": "hit",
            },
            "Q": {
                "basic": "hit",
            },
            "K": {
                "basic": "hit",
            },
            "A": {
                "basic": "hit",
            },
        },
        2: {
            2: {
                "basic": "stay",
            },
            3: {
                "basic": "stay",
            },
            4: {
                "basic": "stay",
            },
            5: {
                "basic": "double",
            },
            6: {
                "basic": "double",
            },
            7: {
                "basic": "hit",
            },
            8: {
                "basic": "hit",
            },
            9: {
                "basic": "hit",
            },
            10: {
                "basic": "hit",
            },
            "J": {
                "basic": "hit",
            },
            "Q": {
                "basic": "hit",
            },
            "K": {
                "basic": "hit",
            },
            "A": {
                "basic": "hit",
            },
        },
    }

    surrender_strategy = {
        15: {
            9: {
                "basic": "play",
                "deviation": ("2+", "surrender")
            },
            10: {
                "basic": "surrender",
                "deviation": ("0-", "play")
            },
            "J": {
                "basic": "surrender",
                "deviation": ("0-", "play")
            },
            "Q": {
                "basic": "surrender",
                "deviation": ("0-", "play")
            },
            "K": {
                "basic": "surrender",
                "deviation": ("0-", "play")
            },
            "A": {
                "basic": "play",
                "deviation": ("-1+", "surrender")
            },
        },
        16: {
            8: {
                "basic": "play",
                "deviation": ("4+", "surrender")
            },
            9: {
                "basic": "surrender",
                "deviation": ("-1-", "play")
            },
            10: {
                "basic": "surrender"
            },
            "J": {
                "basic": "surrender"
            },
            "Q": {
                "basic": "surrender"
            },
            "K": {
                "basic": "surrender"
            },
            "A": {
                "basic": "surrender"
            },
        },
        17: {
            "A": {
                "basic": "surrender"
            }
        }
    }

    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def receive_card(self, card: Card):
        return self.hand.append(card)

    def check_initial_hand(self):
        if len(self.hand) == 2:
            card_values = [card.value for card in self.hand]
            card_types = [card.card_type for card in self.hand]

            if "A" in card_types:
                if 10 in card_values:
                    hand_type = "black jack"
                else:
                    hand_type = "soft"
            elif card_values[0] == card_values[1]:
                hand_type = "pair"
            else:
                if sum(card_values) in (15, 16, 17):
                    hand_type = "surrender"
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
