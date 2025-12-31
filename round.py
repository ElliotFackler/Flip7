import random

class Round:
    def __init__(self):
        self.discard_pile = []

        #self.turn_over = {name: False for name in player_names}

    def create_deck(self):
        # Generates a standard Flip7 deck with number cards 1 - 12, point modifiers, multiplier, and action cards.
        deck = []

        # Add the 78 number cards to the deck.
        for i in range (1, 13):
            for j in range (1, i):
                deck.append({"Type": "Number", "Value": i})

        # Add the nine action cards to the deck.
        for i in range (1, 4):
            deck.append({"Type": "Action", "Value": "FREEZE!"})
            deck.append({"Type": "Action", "Value": "SECOND CHANCE!"})
            deck.append({"Type": "Action", "Value": "FLIP THREE!"})

        # Add the five additive point modifier cards and one multiplier point modifier card to the deck.
        deck.append({"Type": "Modifier", "Value": "+2"})
        deck.append({"Type": "Modifier", "Value": "+4"})
        deck.append({"Type": "Modifier", "Value": "+6"})
        deck.append({"Type": "Modifier", "Value": "+8"})
        deck.append({"Type": "Modifier", "Value": "+10"})
        deck.append({"Type": "Multiplier", "Value": "x2"})


        random.shuffle(deck)
        return deck
    
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
