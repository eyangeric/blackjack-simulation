class Card:
    def __init__(self, card_type):
        if isinstance(card_type, int):
            self.valule = card_type 
        elif isinstance(card_type, str):
            if card_type == 'A':
                self.value = (1, 11)
            else:
                self.value = 10
