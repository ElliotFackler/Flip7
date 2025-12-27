from play import play_game

# Simulating the card game flip 7 created by Eric Olsen

def main():
    # boolean check on game
    is_game_over = False

    # Create the score values.
    player_score = 0
    npc_score = 0

    # Each loop is one round of the game
    while (is_game_over == False):
        # Start a new round
        print("New Round Begin - Player Score:", player_score, "NPC Score:", npc_score)
        player_temp_score, npc_temp_score = play_game()

        player_score += player_temp_score
        npc_score += npc_temp_score

        # Check if either player has reached a score worthy of victory.
        if (player_score >= 200 and player_score > npc_score):
            print("Congratulations! You've won the game with a total score of", player_score)
            is_game_over = True
        elif (npc_score >= 200 and player_score < npc_score):
            print("You've lost the game. The computer has won the game with a score of", npc_score)
            is_game_over = True




if __name__ == "__main__":
    main()