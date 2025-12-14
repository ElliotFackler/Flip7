import random
from main import *


def play_game(deck, player_score, npc_score):
    # Create stuff
    is_round_over = False
    is_player_turn_over = False
    is_npc_turn_over = False
    cards_drawn = []
    chosen_card = ""
    number_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    bonus_points = ["+2", "+4", "+6", "+8", "+10"]
    multiplier = 1

    # Begin the new round
    print("New Round Begin - Player Score:", player_score, "NPC Score:", npc_score)


    while not is_round_over:

        while not is_player_turn_over:
            # Check player input
            player_input = input("Would you like a new card? Y or N \n")


            # Check if the player wants a new card or if he/she would like to end his/her part in the round.
            if (player_input == "N" or player_input == "n"):
                is_round_over = True
                is_player_turn_over = True

                # Count up player's points for the round.
                player_score = player_score + sum(cards_drawn)

            elif (player_input == "Y" or player_input == "y"):
                chosen_card_index = random.randrange(len(deck))
                chosen_card = deck.pop(chosen_card_index)
                
                if (chosen_card in cards_drawn and chosen_card in number_cards): # The player draws a card that he/she has already drawn
                    print("You drew a card that you already have:", chosen_card)
                    is_round_over = True
                    is_player_turn_over = True
                    cards_drawn = []
                    break
                elif (chosen_card in bonus_points): # The player draws an additive point modifier card
                    player_score = player_score + int(chosen_card[1])
                elif (chosen_card == "FREEZE"): # The player draws a freeze card
                    print("FREEZE")
                    is_npc_turn_over = True
                elif (chosen_card == "x2"):
                    multiplier = 2

                else: # The player draws a number card
                    cards_drawn.append(chosen_card)

                print("Your card is", chosen_card)
            else:
                print("That input is not valid")
                continue

            if (len(cards_drawn) >= 7): # Player has reached seven number cards. This means that the round is over and the player gets 15 extra points
                print("You've reached seven number cards. The round is over.")
                is_round_over = True
                is_player_turn_over = True
                is_npc_turn_over = True
                player_score = player_score + 15

        while not is_npc_turn_over:

            chosen_card_index = random.randrange(len(deck))
            chosen_card = deck.pop(chosen_card_index)
                
            if (chosen_card in cards_drawn and chosen_card in number_cards): # The NPC draws a card that he/she has already drawn
                print("The NPC drew a card that he already has:", chosen_card)
                is_round_over = True
                is_npc_turn_over = True
                cards_drawn = []
                break
            elif (chosen_card in bonus_points): # The NPC draws an additive point modifier card
                npc_score = npc_score + int(chosen_card[1])
            elif (chosen_card == "FREEZE"): # The NPC draws a freeze card
                print("FREEZE")
                is_player_turn_over = True
            elif (chosen_card == "x2"):
                multiplier = 2

            else: # The NPC draws a number card
                cards_drawn.append(chosen_card)

                
            print("The NPC's card is", chosen_card)

        if (len(cards_drawn) >= 7): # NPC has reached seven number cards. This means that the round is over and the NPC gets 15 extra points
            is_round_over = True
            is_player_turn_over = True
            is_npc_turn_over = True
            npc_score = npc_score + 15

            # TODO: Put in no card option


            # TODO: Put in yes card option.

            # NPC's card choice
            print("The NPC's card is")
        
            # Check if the NPC busts
            # Check if the NPC has seven number cards.

        print("Your card count for this round is ", sum(cards_drawn) * multiplier)
        print("The cards you have drawn so far this round are: ", cards_drawn, "\n")

    return player_score, npc_score


    

