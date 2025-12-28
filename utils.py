import random

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