from utils import *
from round import * 

def play_game():
    # Create stuff
    round = Round()
    deck2 = round.create_deck()
    playerList = [HumanPlayer(), NPCPlayer()]

    while not playerList[0].info.is_turn_over or not playerList[1].info.is_turn_over:
        for player in playerList:
            if not player.info.is_turn_over:
                choice = player.chooseAction()

                if (choice == "n"):
                    player.info.is_turn_over = True
                    player.info.score = calculate_score(player.info.number_cards_drawn, player.info.multiplier, player.info.score, 0)
                elif (choice == "y"):
                    card, deck2 = round.draw_a_card(deck2)
                    if (card["Type"] == "Number" and card["Value"] in player.info.number_cards_drawn): # The player draws a card that he/she has already drawn
                        print("The player", player.info.name,  "drew a card that you already have:", card["Value"])
                        if (player.info.second_chance == False):
                            player.info.is_turn_over = True
                            player.info.cards_drawn = []
                            player.info.score = 0
                        else:
                            print("Player 1 has used his/her second chance.")
                            player.info.second_chance = False
                    elif (has_bonus_points(card["Value"])): # The player draws an additive point modifier card
                        player.info.score = player.info.score + add_bonus_points(card["Value"])
                    elif (has_freeze(card["Value"])): # The player draws a freeze card
                        print("FREEZE!")
                        player.info.is_turn_over = True
                    elif (has_flip_three(card["Value"])):
                        print("FLIP THREE!")
                        # TODO: Set up flip three
                    elif (has_second_chance(card["Value"])):
                        print("SECOND CHANCE!")
                        player.info.second_chance = True
                        # TODO: Set up second chance.
                    elif (has_multiplier(card["Value"])):
                        player.info.multiplier = 2
                    else: # The player draws a number card
                        player.info.number_cards_drawn.append(card["Value"])

                    round.discard_pile.append(card)
                    player.info.cards_drawn.append(card["Value"])
                    print("The player", player.info.name, " drew card", card["Value"])
                else:
                    print("That input is not valid")
                    continue

                if (has_flipped_seven(player.info.number_cards_drawn)): # Player has reached seven number cards. This means that the round is over and the player gets 15 extra points
                    print("You've reached seven number cards. The round is over.")
                    player.info.is_turn_over = True
                    playerList[1].info.is_turn_over = True
                    playerList[0].info.is_turn_over = True
                    #player2.is_turn_over = True Add other player turn end.
                    player.info.score = calculate_score(player.info.number_cards_drawn, player.info.multiplier, player.info.score, 15)

                print("The cards that", player.info.name, " has drawn so far this round are: ", player.info.cards_drawn, "\n")

    return playerList[0].info.score, playerList[1].info.score








    

