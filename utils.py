def calculate_score(number_card_sum, multiplier, bonus_points, seven_card_bonus):
    return sum(number_card_sum) * multiplier + bonus_points + seven_card_bonus

def has_flipped_seven(cards):
    if (len(cards) >= 7):
        return True
    else:
        return False