from art import logo, vs
from game_data import data
from random import choice
from os import system
from copy import deepcopy


def game():
    score = 0
    wrong = False
    player_choice = True
    game_data = deepcopy(data)
    data_a = choice(game_data)
    data_b = choice(game_data)
    game_data.remove(data_a)
    while player_choice:
        game_data.remove(data_b)
        system('cls')
        print(logo)
        if wrong:
            print(f"Sorry, that's wrong. Final Score: {score}")
            return
        if score != 0:
            print(f"You're right! Current Score: {score}")
        print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.")
        print(vs)
        print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.")
        who_has_more = 'A' if data_a['follower_count'] > data_b['follower_count'] else 'B'
        question = input("Who has more followers? Type 'A' or 'B': ").upper()
        if question in ['A', 'B']:
            if question == who_has_more:
                score += 1
                data_a = data_b
                data_b = choice(game_data)
            else:
                wrong = True
                data_b = choice(game_data)


game()
