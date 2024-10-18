import art
import random

def select_random_number():
    return random.randint(1, 100)

def check_number(number, guess):
    if number == guess:
        return True
    elif number > guess:
        print("Too low")
    else:
        print("Too high")
    return False

def guess_number():
    guess = input("I'm thinking of a number between 1 and 100. Can you guess it? ")
    return int(guess)

def difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    while difficulty not in ["easy", "hard"]:
        difficulty = input("Invalid input. Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        return 10
    else:
        return 5

def main() -> None:
    print(art.logo)
    print("Welcome to the Number Guessing Game!")

    number = select_random_number()
    attempts = difficulty()
    print(f"You have {attempts} attempts to guess the number.")
    while attempts > 0:
        if check_number(number, guess_number()):
            print(f"You got it! The answer was {number}.")
            play_again = input("Do you want to play again? Type 'y' or 'n': ")
            if play_again == "y":
                break
            else:
                print("Goodbye!")
                return None
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

    print(f"You've run out of guesses. The number was {number}.")
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    while play_again == "y":
        main()

    print("Goodbye!")
    return None

if __name__ == "__main__":
    main()