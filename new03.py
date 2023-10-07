import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of player (2 -4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        current_score = 0

        while True:
            should_roll = input("world you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("you rolled a 1! Turn done!")
                current_score = 0
            else:
                currwnt_score+= value
                print("you rolled a:", value) 

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("your total is:", player_scores[player_idx])           
                