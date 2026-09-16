import random

# Snakes: head -> tail
snakes = {
    99: 54,
    95: 75,
    92: 88,
    47: 26,
    25: 7
}

# Ladders: bottom -> top
ladders = {
    2: 23,
    8: 34,
    20: 77,
    32: 68,
    41: 79
}


def roll_dice():
    return random.randint(1, 6)


def move_player(position):
    dice = roll_dice()
    print(f"Dice rolled: {dice}")

    if position + dice <= 100:
        position += dice

    # Check ladder
    if position in ladders:
        print(f"🪜 Ladder! {position} -> {ladders[position]}")
        position = ladders[position]

    # Check snake
    elif position in snakes:
        print(f"🐍 Snake! {position} -> {snakes[position]}")
        position = snakes[position]

    return position


def play_game():
    player1 = 0
    player2 = 0

    print("=== SNAKE AND LADDER GAME ===")

    while True:

        # Player 1
        input("\nPlayer 1: Press Enter to roll dice...")
        player1 = move_player(player1)
        print("Player 1 position:", player1)

        if player1 == 100:
            print("\n🏆 Player 1 wins!")
            break

        # Player 2
        input("\nPlayer 2: Press Enter to roll dice...")
        player2 = move_player(player2)
        print("Player 2 position:", player2)

        if player2 == 100:
            print("\n🏆 Player 2 wins!")
            break


play_game()
