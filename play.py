from utils import *
from round import * 

def play_game():
    # Create stuff
    round = Round()

    deck2 = round.create_deck()


    print(deck2)

    player1 = Player("Player 1")
    player2 = Player("NPC")


    while not player1.is_turn_over or not player2.is_turn_over:
        if not player1.is_turn_over:
            player_input = input("Would you like a new card? Y or N \n")

            # Check if the player wants a new card or if he/she would like to end his/her part in the round.
            if (player_input == "N" or player_input == "n"):
                player1.is_turn_over = True

                # Count up player's points for the round.
                player1.score = calculate_score(player1.number_cards_drawn, player1.multiplier, player1.score, 0)

            elif (player_input == "Y" or player_input == "y"):
                card, deck2 = round.draw_a_card(deck2)
                
                if (card["Type"] == "Number" and card in player1.number_cards_drawn): # The player draws a card that he/she has already drawn
                    print("You drew a card that you already have:", card)
                    player1.is_turn_over = True
                    player1.cards_drawn = []
                    player1.score = 0
                elif (has_bonus_points(card)): # The player draws an additive point modifier card
                    player1.score = player1.score + add_bonus_points(card)
                elif (has_freeze(card)): # The player draws a freeze card
                    print("FREEZE!")
                    player2.is_turn_over = True
                elif (has_flip_three(card)):
                    print("FLIP THREE!")
                    # TODO: Set up flip three
                elif (has_second_chance(card)):
                    print("SECOND CHANCE!")
                    # TODO: Set up second chance.
                elif (has_multiplier(card)):
                    player1.multiplier = 2
                else: # The player draws a number card
                    player1.number_cards_drawn.append(card)

                player1.cards_drawn.append(card)
                print("Your card is", card)
            else:
                print("That input is not valid")
                continue

            if (has_flipped_seven(player1.number_cards_drawn)): # Player has reached seven number cards. This means that the round is over and the player gets 15 extra points
                print("You've reached seven number cards. The round is over.")
                player1.is_turn_over = True
                player2.is_turn_over = True
                player1.score = calculate_score(player1.number_cards_drawn, player1.multiplier, player1.score, 15)

        if not player2.is_turn_over:
            card, deck2 = round.draw_a_card(deck2)

            if (card in player2.number_cards_drawn): # The NPC draws a card that he/she has already drawn
                print("The NPC drew a card that he already has:", card)
                player2.is_turn_over = True
                player2.cards_drawn = []
                player2.score = 0
            elif (has_bonus_points(card)): # The NPC draws an additive point modifier card
                player2.score = player2.score + add_bonus_points(card)
            elif (has_freeze(card)): # The NPC draws a freeze card
                print("FREEZE!")
                player1.is_turn_over = True
            elif (has_flip_three(card)):
                print("FLIP THREE!")
                # TODO: Set up actual flip three stuff
            elif (has_second_chance(card)):
                print("SECOND CHANCE!")
                # TODO: Set up second chance.
            elif (has_multiplier(card)): # The NPC draws the multiplier
                player2.multiplier = 2
            else: # The NPC draws a number card
                player2.number_cards_drawn.append(card)

            player2.cards_drawn.append(card)    
            print("The NPC's card is", card)

            if (has_flipped_seven(player2.number_cards_drawn)): # NPC has reached seven number cards. This means that the round is over and the NPC gets 15 extra points
                player1.is_turn_over = True
                player2.is_turn_over = True
                player2.score = calculate_score(player2.number_cards_drawn, player2.multiplier, player2.score, 15)

        print("The cards you have drawn so far this round are: ", player1.cards_drawn, "\n")
        print("The cards the NPC has drawn so far this round are: ", player2.cards_drawn, "\n")

    return player1.score, player2.score








    

