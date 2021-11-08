from art import logo, vs
from game_data import data
from random import choice
import os


def clear():
    return os.system('clear')


def format_data(account):
    """Takes the account data and returns printable format"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, follower_count_a, follower_count_b):
    """Take the user guess and follower counts and returns if they got it right"""
    if follower_count_a > follower_count_b:
        return guess == "a"  # True id a, False if b
    else:
        return guess == "b"


def game():
    item_b = choice(data)
    score = 0
    continue_game = True

    while continue_game:
        item_a = item_b
        item_b = choice(data)

        while item_a == item_b:
            item_b = choice(data)

        print(f"Compare A: {format_data(item_a)}")
        print(vs)
        print(f"Against B: {format_data(item_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        follower_count_a = item_a['follower_count']
        follower_count_b = item_b['follower_count']
        is_correct = check_answer(guess, follower_count_a, follower_count_b)

        clear()
        print(logo)

        if is_correct:
            score += 1
            print(f"You are right! Current score: {score}")

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False


print(logo)
game()
