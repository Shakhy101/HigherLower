from art import logo, vs
from game_data import data
from random import randint

# vyber nahodny dict z listu - nejprve nahodne cislo od 0 do len(list -1)
def pick_item():
    random_index = randint(0, len(data) - 1)
    return data[random_index]
    


def game():
# na zacatku potrebuji vybrat 2 itemy
    item_a = pick_item()

    
    score = 0
    continue_game = True
    while continue_game:
# vytisknout Compare A Against B
        print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
        item_b = pick_item()
        
        print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")

        # ziskat guess od uzivatele:
        player_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # analyzuj co vybral uzivatel a podle toho urcim 1 - pocet followeru co vybral uzivatel vs pocet followeru druheho listu
        if player_guess == "A":
            follower_count_player = item_a['follower_count']
            follower_count_computer = item_b['follower_count']
        else:
            follower_count_player = item_b['follower_count']
            follower_count_computer = item_a['follower_count']

        print(f"follower by player: {follower_count_player}")
        print(f"follower by computer: {follower_count_computer}")

        # urci kdo ma pravdu

        if follower_count_player > follower_count_computer:
            #you are right, pripocti bod
            score += 1
            print(f"You are right! Current score: {score}")
            item_a = item_b
        else:
            # wrong, print final score, game over
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False
        

        

game()



