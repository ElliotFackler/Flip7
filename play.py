from utils import *
from round import *

def play_game(game_state):
    # Create stuff
    round = Round()
    game_state.deck = game_state.create_deck()
    playerList = [HumanPlayer(), NPCPlayer()]

    while not playerList[0].info.is_turn_over or not playerList[1].info.is_turn_over:
        for player in playerList:
            if not player.info.is_turn_over:
                choice = player.chooseAction()

                if (choice == "n"):
                    player.info.is_turn_over = True
                    player.info.score = calculate_score(player.info.number_cards_drawn, player.info.multiplier, player.info.score, 0)
                elif (choice == "y"):
                    game_state.card, game_state.deck = round.draw_a_card(game_state.deck)

                    if (game_state.card["Value"] in player.info.number_cards_drawn): # The player draws a card that he/she has already drawn
                        print(player.info.name, "busted.")
                        if (player.info.second_chance == False):
                            player.info.is_turn_over = True
                            player.info.cards_drawn = []
                            player.info.score = 0
                        else:
                            print(player.info.name, "has used his/her second chance.")
                            player.info.second_chance = False

                    game_state.card["Type"].apply(player.info, game_state)

                    game_state.discard_pile.append(game_state.card)
                    player.info.cards_drawn.append(game_state.card["Value"])
                    print(player.info.name, "drew card", game_state.card["Value"])
                else:
                    print("That input is not valid")
                    continue

                if (has_flipped_seven(player.info.number_cards_drawn)): # Player has reached seven number cards. This means that the round is over and the player gets 15 extra points
                    print(player.info.name, "reached seven number cards. The round is over.")
                    player.info.is_turn_over = True
                    playerList[1].info.is_turn_over = True
                    playerList[0].info.is_turn_over = True
                    player.info.score = calculate_score(player.info.number_cards_drawn, player.info.multiplier, player.info.score, 15)
                print("The cards that", player.info.name, "has drawn so far this round are: ", player.info.cards_drawn, "\n")

    game_state.player_score += playerList[0].info.score
    game_state.npc_score += playerList[1].info.score








    

