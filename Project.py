# Imports
import random
import requests
import time

# Definitions
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
    'name': pokemon['name'],
    'id': pokemon['id'],
    'height': pokemon['height'],
    'weight': pokemon['weight']
    }

# Game beginning
print("Welcome to Pokemon Top Trumps!")
print("Your pokemon is...")

# Generate a random number between 1 and 151 to use as the Pokemon ID number:
pokemon_number = (random.randint(1,151))

# Using the Pokemon API get a Pokemon based on its ID number:
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

# Create a dictionary that contains the returned pokemon's name, id, height and weight:
response = requests.get(url)
pokemon = response.json()

# Display the pokemon and its stats to the player.
print(pokemon["name"])
time.sleep(2)
print("ID Number:")
print(pokemon["id"])
print("Height:")
print(pokemon["height"])
print("Weight:")
print(pokemon["weight"])

time.sleep(2)

# Ask the user which stat they want to use (id, height or weight)
print("It's time to play.")
print("Pick a stat (ID, Height, Weight).")
print("If it's higher than your opponent's, you win!")
print("If it's lower, you lose.")
print("If it's the same, you draw.")
time.sleep(2)
input("Which stat do you want to use?")

# Allow the user to decide on a stat for comparison (to do)
#
#
#

# Get another random pokemon for their opponent and display its stats:
print("The opponent's pokemon is...")
pokemon_number = (random.randint(1,151))
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
pokemon = response.json()
print(pokemon["name"])
time.sleep(2)
print("ID Number:")
print(pokemon["id"])
print("Height:")
print(pokemon["height"])
print("Weight:")
print(pokemon["weight"])

# Return a win, lose or draw result (to do)
#
#
#