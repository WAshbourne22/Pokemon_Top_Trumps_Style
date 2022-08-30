import random
import requests
import time


# Function to collect random pokemon
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }


# added a score function
def updateScore(score):
    score += 1
    return score


# added some variables so that we can display the score at the bottom.
# counter so that we can play the game 3 times
my_score = 0
opponent_score = 0
counter = 1


# function to output the final winner
def calcScore(my_score, opponent_score):
    if my_score == opponent_score:
        print("\nWe have a tie")
    elif opponent_score > my_score:
        print("\nIn best out of three, the computer beat you")
    else:
        print("\nIn best out of three, you beat the computer! Congrats!!")


# Game Intro
# Printing out Pokemon name along with stats
print("Welcome to Pokemon Top Trumps!")
time.sleep(2)
print("\nPick a stat (ID, Height, Weight).")
print("If it's higher than your opponent's, you win!")
time.sleep(2)
print("It's time to play, best out of 3!")


# High Score Programme

def get_high_score():
    # Default high score
    high_score = 0

    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("\nThe high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("\nThere is no high score yet.")
    except ValueError:
        # There's a file there, but it doesn't understand the number.
        print("\nI'm confused. Starting with no high score.")

    return high_score


def save_high_score(new_high_score):
    try:
        # Write the file to disk
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Can't write it.
        print("Unable to save the high score.")


def main():
    """ Main programme is here. """
    # Get the high score
    high_score = get_high_score()

    # Get the score from the current game
    current_score = 0
    try:
        # Ask the user for their score
        current_score = int(input("\nWhat is your score? "))
    except ValueError:
        # Error, they didn't type a number
        print("\nI don't understand what you typed.")

    # See if we have a new high score
    if current_score > high_score:
        # Yes: save to file
        print("\nYay! New high score!")
        save_high_score(current_score)


# Counter to allow the game to be played 3 times.
# This can be changed should we want there to be more than 3 rounds
while counter < 4:

    # User's pokemon
    print("\nYour pokemon is...")

    my_pokemon = random_pokemon()
    print(my_pokemon["name"])
    time.sleep(2)
    print("ID Number:")
    print(my_pokemon["id"])
    print("Height:")
    print(my_pokemon["height"])
    print("Weight:")
    print(my_pokemon["weight"])

    time.sleep(2)

    # Allow user to choose which stat they would like to choose
    stat_choice = input("\nWhich stat do you want to use? (id, height, weight) ").lower()

    # Printing out opponent pokemon along with stats
    print("\nYour opponent's pokemon is...")
    opponent_pokemon = random_pokemon()
    my_pokemon = random_pokemon()
    print(opponent_pokemon["name"])
    time.sleep(2)
    print("ID Number:")
    print(opponent_pokemon["id"])
    print("Height:")
    print(opponent_pokemon["height"])
    print("Weight:")
    print(opponent_pokemon["weight"])
    time.sleep(2)

    # Using the stat choice chosen by the user to generate a comparison
    my_stat = int(my_pokemon[stat_choice])
    opponent_stat = int(opponent_pokemon[stat_choice])

    # Correct if statements for win, lose or draw
    # and update score
    if my_stat > opponent_stat:
        print("\nCongratulations, you win this round")
        my_score = updateScore(my_score)
        print("\nYour score: ", my_score, "Computer score: ", opponent_score)
    elif my_stat < opponent_stat:
        print("\nNo win this time")
        opponent_score = updateScore(opponent_score)
        print("\nYour score: ", my_score, "Computer score: ", opponent_score)
    else:
        print("Better luck next time.")
        print('\nIt looks like a Draw!')

    counter += 1

# Call the main function, start up the game
if __name__ == "__main__":
    main()
# call function to output final winner from the game (all 3 rounds)
calcScore(my_score, opponent_score)
