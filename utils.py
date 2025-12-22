import random

def create_deck():
    # Create the base deck.
    deck = [0]

    # Add the number of each card to the deck.
    for i in range (1, 13):
        deck = deck + ([i] * i)

    # Create the action cards and the point modifier cards.
    deck.append("FREEZE!")
    deck.append("FREEZE!")
    deck.append("FREEZE!")
    deck.append("FLIP THREE!")
    deck.append("FLIP THREE!")
    deck.append("FLIP THREE!")
    deck.append("SECOND CHANCE!")
    deck.append("SECOND CHANCE!")
    deck.append("SECOND CHANCE!")
    deck.append("+2")
    deck.append("+4")
    deck.append("+6")
    deck.append("+8")
    deck.append("+10")
    deck.append("x2")
    return deck

def draw_a_card(deck): # Pick another card randomly from the deck.
    print("Card drawn")
    index = random.randrange(len(deck))
    card_drawn = deck.pop(index)
    return card_drawn, deck