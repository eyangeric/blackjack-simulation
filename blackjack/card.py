class Card:
    def __init__(self, card_type):
        self.card_type = card_type
        if isinstance(card_type, int):
            self.value = card_type
            if card_type >= 2 and card_type < 7:
                self.count_value = 1
            elif card_type == 10:
                self.count_value = -1
            else:
                self.count_value = 0
        elif isinstance(card_type, str):
            self.count_value = -1
            if card_type == "A":
                self.value = (1, 11)
            else:
                self.value = 10
