from play import *

# Simulating the card game flip 7 created by Eric Olsen


def main():
    # boolean check on game
    is_game_over = False

    # Create the score values.
    player_score = 0
    npc_score = 0

    # Create the base deck.
    deck = [0]

    # Add the number of each card to the deck.
    for i in range (1, 13):
        deck = deck + ([i] * i)

    # Create the action cards and the point modifier cards.
    deck.append("FREEZE")
    deck.append("FREEZE")
    deck.append("FREEZE")
    deck.append("FLIP THREE")
    deck.append("FLIP THREE")
    deck.append("FLIP THREE")
    deck.append("SECOND CHANCE")
    deck.append("SECOND CHANCE")
    deck.append("SECOND CHANCE")
    deck.append("+2")
    deck.append("+4")
    deck.append("+6")
    deck.append("+8")
    deck.append("+10")
    deck.append("x2")


    # Each loop is one round of the game
    while (is_game_over == False):
        # Start a new round
        player_score, npc_score = play_game(deck, player_score, npc_score)

        # Check if either player has reached a score worthy of victory.
        if (player_score >= 200 and player_score > npc_score):
            print("Congratulations! You've won the game with a total score of", player_score)
            is_game_over = True
        elif (npc_score >= 200 and player_score < npc_score):
            print("You've lost the game. The computer has won the game with a score of", npc_score)
            is_game_over = True



if __name__ == "__main__":
    main()