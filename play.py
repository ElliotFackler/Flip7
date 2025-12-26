from utils import *

def play_game(full_deck):
    # Create stuff
    is_player_turn_over = False
    is_npc_turn_over = False
    cards_drawn = []
    player_number_cards_drawn = []
    npc_cards_drawn = []
    npc_number_cards_drawn = []
    multiplier = 1
    npc_multiplier = 1
    player_score = 0
    npc_score = 0

    while not is_player_turn_over or not is_npc_turn_over:
        if not is_player_turn_over:
            player_input = input("Would you like a new card? Y or N \n")

            # Check if the player wants a new card or if he/she would like to end his/her part in the round.
            if (player_input == "N" or player_input == "n"):
                is_player_turn_over = True

                # Count up player's points for the round.
                player_score = calculate_score(player_number_cards_drawn, multiplier, player_score, 0)

            elif (player_input == "Y" or player_input == "y"):
                chosen_card, full_deck = draw_a_card(full_deck)
                
                if (chosen_card in player_number_cards_drawn): # The player draws a card that he/she has already drawn
                    print("You drew a card that you already have:", chosen_card)
                    is_player_turn_over = True
                    cards_drawn = []
                    player_score = 0
                elif (has_bonus_points(chosen_card)): # The player draws an additive point modifier card
                    player_score = player_score + add_bonus_points(chosen_card)
                elif (has_freeze(chosen_card)): # The player draws a freeze card
                    print("FREEZE!")
                    is_npc_turn_over = True
                elif (has_flip_three(chosen_card)):
                    print("FLIP THREE!")
                    # TODO: Set up flip three
                elif (has_second_chance(chosen_card)):
                    print("SECOND CHANCE!")
                    # TODO: Set up second chance.
                elif (has_multiplier(chosen_card)):
                    multiplier = 2
                else: # The player draws a number card
                    player_number_cards_drawn.append(chosen_card)

                cards_drawn.append(chosen_card)
                print("Your card is", chosen_card)
            else:
                print("That input is not valid")
                continue

            if (has_flipped_seven(player_number_cards_drawn)): # Player has reached seven number cards. This means that the round is over and the player gets 15 extra points
                print("You've reached seven number cards. The round is over.")
                is_player_turn_over = True
                is_npc_turn_over = True
                player_score = calculate_score(player_number_cards_drawn, multiplier, player_score, 15)

        if not is_npc_turn_over:
            npc_chosen_card, full_deck = draw_a_card(full_deck)

            if (npc_chosen_card in npc_number_cards_drawn): # The NPC draws a card that he/she has already drawn
                print("The NPC drew a card that he already has:", npc_chosen_card)
                is_npc_turn_over = True
                npc_cards_drawn = []
                npc_score = 0
            elif (has_bonus_points(npc_chosen_card)): # The NPC draws an additive point modifier card
                npc_score = npc_score + add_bonus_points(npc_chosen_card)
            elif (has_freeze(npc_chosen_card)): # The NPC draws a freeze card
                print("FREEZE!")
                is_player_turn_over = True
            elif (has_flip_three(npc_chosen_card)):
                print("FLIP THREE!")
                # TODO: Set up actual flip three stuff
            elif (has_second_chance(npc_chosen_card)):
                print("SECOND CHANCE!")
                # TODO: Set up second chance.
            elif (has_multiplier(npc_chosen_card)): # The NPC draws the multiplier
                npc_multiplier = 2
            else: # The NPC draws a number card
                npc_number_cards_drawn.append(npc_chosen_card)

            npc_cards_drawn.append(npc_chosen_card)    
            print("The NPC's card is", npc_chosen_card)

            if (has_flipped_seven(npc_number_cards_drawn)): # NPC has reached seven number cards. This means that the round is over and the NPC gets 15 extra points
                is_player_turn_over = True
                is_npc_turn_over = True
                npc_score = calculate_score(npc_number_cards_drawn, npc_multiplier, npc_score, 15)
     

        print("The cards you have drawn so far this round are: ", cards_drawn, "\n")
        print("The cards the NPC has drawn so far this round are: ", npc_cards_drawn, "\n")

    return player_score, npc_score








    

