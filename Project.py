import random
import requests

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

def run():
    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
stat_choice = input('Which stat do you want to use? (id, height, weight) ')
opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))

my_stat = my_pokemon[stat_choice]
opponent_stat = opponent_pokemon[stat_choice]

if my_stat > opponent_stat:
    print('You Win!')
elif my_stat < opponent_stat:
    print('You Lose!')
else:
    print('Draw!')

run()

# print("Welcome to Pokemon Top Trumps!")
# print("Player 1, your pokemon is...")
#
# #1. Generate a random number between 1 and 151 to use as the Pokemon ID number:
# pokemon_number = (random.randint(1,151))
#
# #2. Using the Pokemon API get a Pokemon based on its ID number:
# url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
#
# #3. Create a dictionary that contains the returned pokemon's name, id, height and weight:
# response = requests.get(url)
# pokemon = response.json()
#
# print(pokemon["name"])
# print("ID Number:")
# print(pokemon["id"])
# print("Height:")
# print(pokemon["height"])
# print("Weight:")
# print(pokemon["weight"])
#
# #4. Get another random pokemon for their opponent:
# print("Player 2, your pokemon is...")
# pokemon_number = (random.randint(1,151))
# url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
# response = requests.get(url)
# pokemon = response.json()
#
# print(pokemon["name"])
# print("ID Number:")
# print(pokemon["id"])
# print("Height:")
# print(pokemon["height"])
# print("Weight:")
# print(pokemon["weight"])
#
# #5. Ask the user which stat they want to use (id, height or weight)
# input("Which stat do you want to use?")