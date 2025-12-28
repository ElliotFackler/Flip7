

class Round:
    def __init__(self):

        self.is_player_turn_over = False
        self.is_npc_turn_over = False

        self.player_number_cards_drawn = []
        self.npc_number_cards_drawn = []

        self.multiplier = 1
        self.npc_multiplier = 1

        self.player_score = 0
        self.npc_score = 0

        self.cards_drawn = []
        self.npc_cards_drawn = []

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