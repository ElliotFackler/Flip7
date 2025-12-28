from utils import *
from round import * 

def play_game():
    # Create stuff
    round = Round()

    deck2 = round.create_deck()


    while not round.is_player_turn_over or not round.is_npc_turn_over:
        if not round.is_player_turn_over:
            player_input = input("Would you like a new card? Y or N \n")

            # Check if the player wants a new card or if he/she would like to end his/her part in the round.
            if (player_input == "N" or player_input == "n"):
                round.is_player_turn_over = True

                # Count up player's points for the round.
                round.player_score = calculate_score(round.player_number_cards_drawn, round.multiplier, round.player_score, 0)

            elif (player_input == "Y" or player_input == "y"):
                chosen_card, deck2 = draw_a_card(deck2)
                
                if (chosen_card in round.player_number_cards_drawn): # The player draws a card that he/she has already drawn
                    print("You drew a card that you already have:", chosen_card)
                    round.is_player_turn_over = True
                    round.cards_drawn = []
                    round.player_score = 0
                elif (has_bonus_points(chosen_card)): # The player draws an additive point modifier card
                    round.player_score = round.player_score + add_bonus_points(chosen_card)
                elif (has_freeze(chosen_card)): # The player draws a freeze card
                    print("FREEZE!")
                    round.is_npc_turn_over = True
                elif (has_flip_three(chosen_card)):
                    print("FLIP THREE!")
                    # TODO: Set up flip three
                elif (has_second_chance(chosen_card)):
                    print("SECOND CHANCE!")
                    # TODO: Set up second chance.
                elif (has_multiplier(chosen_card)):
                    round.multiplier = 2
                else: # The player draws a number card
                    round.player_number_cards_drawn.append(chosen_card)

                round.cards_drawn.append(chosen_card)
                print("Your card is", chosen_card)
            else:
                print("That input is not valid")
                continue

            if (has_flipped_seven(round.player_number_cards_drawn)): # Player has reached seven number cards. This means that the round is over and the player gets 15 extra points
                print("You've reached seven number cards. The round is over.")
                round.is_player_turn_over = True
                round.is_npc_turn_over = True
                round.player_score = calculate_score(round.player_number_cards_drawn, round.multiplier, round.player_score, 15)

        if not round.is_npc_turn_over:
            npc_chosen_card, deck2 = draw_a_card(deck2)

            if (npc_chosen_card in round.npc_number_cards_drawn): # The NPC draws a card that he/she has already drawn
                print("The NPC drew a card that he already has:", npc_chosen_card)
                round.is_npc_turn_over = True
                round.npc_cards_drawn = []
                round.npc_score = 0
            elif (has_bonus_points(npc_chosen_card)): # The NPC draws an additive point modifier card
                round.npc_score = round.npc_score + add_bonus_points(npc_chosen_card)
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
                round.npc_multiplier = 2
            else: # The NPC draws a number card
                round.npc_number_cards_drawn.append(npc_chosen_card)

            round.npc_cards_drawn.append(npc_chosen_card)    
            print("The NPC's card is", npc_chosen_card)

            if (has_flipped_seven(round.npc_number_cards_drawn)): # NPC has reached seven number cards. This means that the round is over and the NPC gets 15 extra points
                round.is_player_turn_over = True
                round.is_npc_turn_over = True
                round.npc_score = calculate_score(round.npc_number_cards_drawn, round.npc_multiplier, round.npc_score, 15)
     

        print("The cards you have drawn so far this round are: ", round.cards_drawn, "\n")
        print("The cards the NPC has drawn so far this round are: ", round.npc_cards_drawn, "\n")

    return round.player_score, round.npc_score








    

