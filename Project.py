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

# Printing out Pokemon name along with stats
print("Welcome to Pokemon Top Trumps!")
print("Pick a stat (ID, Height, Weight).")
print("If it's higher than your opponent's, you win!")
print("If it's lower, you lose.")
print("If it's the same, you draw.")
print("Your pokemon is...")

my_pokemon = random_pokemon()
print(my_pokemon["name"])
time.sleep(2)
print("ID Number:")
print(my_pokemon["id"])
print("Height:")
print(my_pokemon["height"])
print("Weight:")
print(my_pokemon["weight"])

# Allow user to choice which stat they would like to choose
stat_choice = input('Which stat do you want to use? (id, height, weight) ').lower()

# Printing out opponent pokemon along with stats
print("Your opponent's pokemon is...")
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

# Using the stat choice chosen by the user to generate a comparison
my_stat = my_pokemon[stat_choice]
opponent_stat = opponent_pokemon[stat_choice]

# If statements for win lose or draw
if my_stat > opponent_stat:
    print('Congratulations, you win!')
elif my_stat < opponent_stat:
    print('No win this time')
else:
    print('It looks like a Draw!')

