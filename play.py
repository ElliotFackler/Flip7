import random
from main import *


def play_game(deck, player_score, npc_score):
    # Create stuff
    is_round_over = False
    cards_drawn = []
    chosen_card = ""
    number_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    bonus_points = ["+2", "+4", "+6", "+8", "+10"]
    multiplier = 1

    # Begin the new round
    print("New Round Begin - Player Score:", player_score, "NPC Score:", npc_score)


    while not is_round_over:
        # Check player input
        player_input = input("Would you like a new card? Y or N \n")


        # Check if the player wants a new card or if he/she would like to end his/her part in the round.
        if (player_input == "N" or player_input == "n"):
            is_round_over = True

            # Count up player's points for the round.
            player_score = player_score + sum(cards_drawn)

        elif (player_input == "Y" or player_input == "y"):
            chosen_card_index = random.randrange(len(deck))
            chosen_card = deck.pop(chosen_card_index)
            
            if (chosen_card in cards_drawn and chosen_card in number_cards): # The player draws a card that he/she has already drawn
                print("You drew a card that you already have:", chosen_card)
                is_round_over = True
                cards_drawn = []
                break
            elif (chosen_card in bonus_points): # The player draws an additive point modifier card
                player_score = player_score + int(chosen_card[1])
            elif (chosen_card == "FREEZE"): # The player draws a freeze card
                print("FREEZE")

                # TODO: Add freezing for NPC.
            
            elif (chosen_card == "x2"):
                multiplier = 2

            else: # The player draws a number card
                cards_drawn.append(chosen_card)

            
            print("Your card is ", chosen_card)
        else:
            print("That input is not valid")
            continue

        if (len(cards_drawn) >= 7): # Player has reached seven number cards. This means that the round is over and the player gets 15 extra points
            is_round_over = True
            player_score = player_score + 15


        # NPC's card choice
        print("The NPC's card is")
        
        # Check if the NPC busts
        # Check if the NPC has seven number cards.

        print("Your card count for this round is ", sum(cards_drawn) * multiplier)
        print("The cards you have drawn so far this round are: ", cards_drawn, "\n")

    return player_score, npc_score


    

