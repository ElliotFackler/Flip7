from play import play_game
import os
from game_state import GameState

# Simulating the card game flip 7 created by Eric Olsen

def main():
    game_state = GameState()

    # Each loop is one round of the game
    while (game_state.is_game_over == False):
        # Start a new round
        print("New Round Begin - Player Score:", game_state.player_score, "NPC Score:", game_state.npc_score)
        play_game(game_state)

        # Check if either player has reached a score worthy of victory.
        if (game_state.player_score >= 200 and game_state.player_score > game_state.npc_score):
            print("Congratulations! You've won the game with a total score of", game_state.player_score)
        elif (game_state.npc_score >= 200 and game_state.player_score < game_state.npc_score):
            print("You've lost the game. The computer has won the game with a score of", game_state.npc_score)
            game_state.is_game_over = True

        #os.system('cls' if os.name == 'nt' else 'clear')




if __name__ == "__main__":
    main()