from utils import create_deck

class Round:
    def __init__(self):
        self.deck = create_deck()

        #self.turn_over = {name: False for name in player_names}