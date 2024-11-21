class Card:
    card_types = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, card_type):
        if card_type not in Card.card_types:
            raise ValueError(f"Invalid card type: {card_type}")
        self.card_type = card_type
        self.value = self.assign_value()
        self.count_value = self.assign_count_value()

    def is_integer(self):
        return self.card_type.isdigit()

    def assign_value(self):
        if self.is_integer():
            return [int(self.card_type)]
        elif self.card_type == "A":
            return [1, 11]
        return [10]

    def assign_count_value(self):
        if self.is_integer():
            return 1 if 2 <= int(self.card_type) < 7 else 0
        return -1

    def __repr__(self):
        return f"Card({self.card_type})"
