import random

def create_deck():
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

def draw_a_card(full_deck): # Pick another card randomly from the deck.

    weights = list(full_deck.values())
    options = list(full_deck.keys())

    card = random.choices(options, weights=weights, k=1)[0]

    full_deck[card] -= 1

    if full_deck[card] == 0:
        del full_deck[card]

    return card, full_deck

def calculate_score(number_card_sum, multiplier, bonus_points, seven_card_bonus):
    return sum(number_card_sum) * multiplier + bonus_points + seven_card_bonus

def add_bonus_points(card):
    return int(card[1])

def has_flipped_seven(cards):
    if (len(cards) >= 7):
        return True
    else:
        return False
    
def has_second_chance(card):
    if (card == "SECOND CHANCE!"):
        return True
    else:
        return False
    
def has_flip_three(card):
    if (card == "FLIP THREE!"):
        return True
    else:
        return False
    
def has_freeze(card):
    if (card == "FREEZE!"):
        return True
    else:
        return False
    
def has_multiplier(card):
    if (card == "x2"):
        return True
    else:
        return False
    
def has_bonus_points(card):
    if (card in ["+2", "+4", "+6", "+8", "+10"]):
        return True
    else:
        return False