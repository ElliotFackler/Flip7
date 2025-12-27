from utils import create_deck

class Round:
    def __init__(self):
        self.deck = create_deck()

        #self.turn_over = {name: False for name in player_names}

    def create_deck(self):
        # Create the base deck.
        full_deck = {}

        # Add the number of each card to the deck.
        for i in range (1, 13):
            full_deck[i] = i


        full_deck["FREEZE!"] = 3
        full_deck["FLIP THREE!"] = 3
        full_deck["FREEZE!"] = 3
        full_deck["SECOND CHANCE!"] = 3
        full_deck["+2"] = 1
        full_deck["+4"] = 1
        full_deck["+6"] = 1
        full_deck["+8"] = 1
        full_deck["+10"] = 1
        full_deck["x2"] = 1

        return full_deck