class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 0
    def reveal_cards(self):
        return {self.hand}