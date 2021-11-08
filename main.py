from art import logo, vs
from game_data import data
from random import randint
import os

def clear():
    return os.system('clear')


def pick_item():
    """Picks random item from list"""
    random_index = randint(0, len(data) - 1)
    return data[random_index]

def process_correct_answer(score):
    score += 1
    print(f"You are right! Current score: {score}")
    return score
            
def game():
    item_a = pick_item()
    score = 0
    continue_game = True
    while continue_game:
        print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
        item_b = pick_item()
        
        while item_a == item_b:
            item_b = pick_item()
        
        print(vs)
        
        print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")
        player_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        clear()
        
        follower_count_a = item_a['follower_count']
        follower_count_b = item_b['follower_count']
        
        print(logo)
        
        if (follower_count_a > follower_count_b and player_guess == "A") or (follower_count_a < follower_count_b and player_guess == "B"):
            score = process_correct_answer(score)
            item_a = item_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False

print(logo)
game()



