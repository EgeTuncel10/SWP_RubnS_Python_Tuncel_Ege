import json
import random


def menu():
    while True:
        print('\n - Play [p]')
        print(' - Statistics [s]')
        print(' - Exit [e]')

        choice = input('Your choice: ')

        if choice.lower() in ['p', 's', 'e']:
            return choice.lower()
        else:
            print('\nInvalid choice. Please choose either [p] for Play or [s] for Statistics.')


def play_or_show(choice, game_rules):
    if choice == 'p':
        player = read_value_from_json_file('../game_data.json', 'player')
        comp = read_value_from_json_file('../game_data.json', 'comp')
        print('\n\nLet\'s play! (rock, paper, scissors, lizard, spock)')
        user_move = input('Your move: ')
        move = comp_select_rand_move()
        print('Comps choice: ' + move)
        if move in game_rules[user_move]:
            print('Congratulations, you won against comp!')
            player["amount_of_wins"] += 1
            player[user_move] += 1
            comp[move] += 1
        elif move == user_move:
            print('It is a draw.')
            comp[move] += 1
            player[user_move] += 1
        else:
            print('Oh, you lost against comp.')
            comp["amount_of_wins"] += 1
            comp[move] += 1
            player[user_move] += 1

        write_to_json_file(comp, '../game_data.json', 'comp')
        write_to_json_file(player, '../game_data.json', 'player')

    elif choice == 's':
        print('\n\nDisplaying statistics...')
        player = read_value_from_json_file('../game_data.json', 'player')
        comp = read_value_from_json_file('../game_data.json', 'comp')
        print('player: ' + str(player))
        print('comp: ' + str(comp))


def comp_select_rand_move():
    moves = ["rock", "paper", "scissors", "lizard", "spock"]
    return random.choice(moves)


def read_value_from_json_file(filename, key):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get(key, None)
    except FileNotFoundError:
        return None


def write_to_json_file(data, filename, key):
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data[key] = data

    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=2)


def main():
    game_rules = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }
    print('Welcome to my Rock, Paper, Scissors, Lizard, Spock game!')
    choice = ''
    while choice != 'e':
        choice = menu()
        if choice.lower() != 'e':
            play_or_show(choice, game_rules)
