from src.models.card import Card
from src.models.hand import Hand
from src.strategy import pair_split_strategy, soft_strategy, surrender_strategy, hard_strategy


class CardCounter:
    def __init__(self):
        self.name = "Card Counter"
        self.hands = [Hand()]

    def receive_initial_hand(self, card: Card):
        self.hands[0].add_card(card)

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

    def choose_starting_strategy(self):
        if self.hand_type == "pair":
            self.strategy = pair_split_strategy
        elif self.hand_type == "soft":
            self.strategy = soft_strategy
        elif self.hand_type == "surrender":
            self.strategy = surrender_strategy
        elif self.hand_type == "hard":
            self.strategy = hard_strategy

    def check_hand_key(self, hand: Hand):
        if self.hand_type == "pair":
            self.hand_key = hand.cards[0].card_type
        elif self.hand_type == "soft":
            self.hand_key = [card.card_type for card in hand.cards if card.card_type != "A"][0]
        else:
            self.hand_key = str(sum([card.value[0] for card in hand.cards]))

    def check_play_strategy(self, dealer_up_card: Card, true_count: int, running_count: int):
        strategy_options = self.strategy.get(self.hand_key).get(dealer_up_card.card_type)
        if not strategy_options and self.hand_type == "surrender":
            self.hand_type = "hard"
            self.strategy = hard_strategy
            strategy_options = self.strategy.get(self.hand_key).get(dealer_up_card.card_type)
        if len(strategy_options) == 1:
            self.play_decision = strategy_options.get("basic")
        else:
            deviation = strategy_options.get("deviation")[0]
            play_strategy = self.check_deviation(deviation=deviation, true_count=true_count, running_count=running_count)
            self.play_decision = strategy_options.get(play_strategy)[1]
        if self.play_decision == "play":
            self.hand_type = "hard"
            self.strategy = hard_strategy
            strategy_options = self.strategy.get(self.hand_key).get(dealer_up_card.card_type)
            if len(strategy_options) == 1:
                self.play_decision = strategy_options.get("basic")
            else:
                deviation = strategy_options.get("deviation")[0]
                play_strategy = self.check_deviation(deviation=deviation, true_count=true_count, running_count=running_count)
                self.play_decision = strategy_options.get(play_strategy)[1]


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