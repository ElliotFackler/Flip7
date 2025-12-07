from play import *

# Simulating the card game flip 7 created by Erik Olson


def main():

    # Create the base deck.
    deck = [0]

    # Add the number of each card to the deck
    for i in range (1, 13):
        deck = deck + ([i] * i)

    print(deck)

    play_game()


if __name__ == "__main__":
    main()