import random

class Number:
    def apply(self, player, card):
        player.number_cards_drawn.append(card)

class Freeze:
    def apply(self, player, card):
        pass

class SecondChance:
    def apply(self, player, card):
        player.second_chance = True

class FlipThree:
    def apply(self, player, card):
        pass

class Modifier:
    def apply(self, player, card):
        player.score += int(card[1])

class Multiplier:
    def apply(self, player, card):
        pass

class GameState:
    def __init__(self):
        self.player_score = 0
        self.npc_score = 0
        self.is_game_over = False
        self.discard_pile = []

    def create_deck(self):
        # Generates a standard Flip7 deck with number cards 1 - 12, point modifiers, multiplier, and action cards.
        deck = []

        # Add the 78 number cards to the deck.
        for i in range (1, 13):
            for j in range (1, i):
                deck.append({"Type": Number(), "Value": i})

        # Add the nine action cards to the deck.
        for i in range (1, 4):
            deck.append({"Type": Freeze(), "Value": "FREEZE!"})
            deck.append({"Type": SecondChance(), "Value": "SECOND CHANCE!"})
            deck.append({"Type": FlipThree(), "Value": "FLIP THREE!"})

        # Add the five additive point modifier cards and one multiplier point modifier card to the deck.
        deck.append({"Type": Modifier(), "Value": "+2"})
        deck.append({"Type": Modifier(), "Value": "+4"})
        deck.append({"Type": Modifier(), "Value": "+6"})
        deck.append({"Type": Modifier(), "Value": "+8"})
        deck.append({"Type": Modifier(), "Value": "+10"})
        deck.append({"Type": Multiplier(), "Value": "x2"})


        random.shuffle(deck)
        return deck
