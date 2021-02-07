import random


def roll_dice(player_num, space_num):
    input(f"Player {player_num}, type 'r' to roll the dice: ")
    dice = random.randint(1, 6)
    space_num += dice
    print(f"\tYou rolled a {dice}")
    print(f"\tMove forward {dice} spaces")
    print(f"\tYou landed on {space_num}")
    if space_num >= 100:
        return 100
    while space_num % 10 == 0 or space_num % 5 == 0:
        if space_num % 10 == 0:
            space_num = 1
            print(f"\tYou landed on a snake! Move back to start!")
        elif space_num % 5 == 0:
            space_num += 9
            print(f"\tYou landed on a ladder! Move forward 9 spaces to {space_num}")
    return space_num


def snakes_and_ladders():
    print("Snakes and Ladders")
    print("Be the first player to get to 100")
    print("Squares ending in 5 are ladders and move you forward 9 spaces!")
    print("Squares ending in 0 (except 100) are snakes amd move you back to start!")

    player1 = 1
    player2 = 1
    while player1 < 100 and player2 < 100:
        player1 = roll_dice(1, player1)
        player2 = roll_dice(2, player2)

    if player1 == 100:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


snakes_and_ladders()