import random
import art
from game_data import data

def get_account():
    account = random.choice(data)
    print(format_data(account))
    return account

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def user_guess():
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    while guess not in ['A', 'B']:
        guess = input("Invalid input. Please type 'A' or 'B': ").upper()
    return guess

def check_guess(account_a, account_b, guess):
    if account_a['follower_count'] > account_b['follower_count']:
        return guess == 'A'
    else:
        return guess == 'B'

def game():
    score = 0
    while True:
        print(art.logo)


        player_guess = check_guess(get_account(), get_account(), user_guess())

        if player_guess:
            score += 1
            print(f"You're right! Current score: {score}.")

        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            quit()

        play_again = input("Would you like to play again? Type 'yes' or 'no': ").lower()
        while play_again not in ['yes', 'no']:
            play_again = input("Invalid input. Please type 'yes' or 'no': ").lower()

        if play_again == 'no':
            print("Goodbye.")
            quit()

game()