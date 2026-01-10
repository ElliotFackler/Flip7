class Round:
    def __init__(self):
        print(" ")

    def draw_a_card(self, deck): # Take the card from the top of the deck
        if(len(deck)>0):
            card = deck.pop(0)
            return card, deck
        else:
            return None, deck
    
class Player:
    def __init__(self, name):
        self.name = name
        self.cards_drawn = []
        self.score = 0
        self.multiplier = 1
        self.is_turn_over = False
        self.number_cards_drawn = []
        self.second_chance = False

class HumanPlayer:
    def __init__(self):
        self.info = Player("Human Player")

    def chooseAction(self):
        player_input = input("Would you like a new card? (y/n)) \n")
        return player_input


class NPCPlayer:
    def __init__(self):
        self.info = Player("NPC Player")

    def chooseAction(self):
        return "y"
