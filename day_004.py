import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock, paper, scissors]

matchups = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

hands = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

def get_user_choice():
    user_choice = input("What do you choose? Type rock, paper or scissors: ").lower()
    while user_choice not in matchups:
        user_choice = input("Invalid choice. Please type rock, paper or scissors: ").lower()
    return user_choice, hands[user_choice]

def get_computer_choice():
    comp_hand = random.choice(list(matchups.keys()))
    return comp_hand, hands[comp_hand]

def determine_winner(user_choice, comp_choice):
    print(f"You chose:\n{user_choice[1]}")
    print(f"Computer chose:\n{comp_choice[1]}")

    if user_choice[0] == comp_choice[0]:
        print("It's a draw!")

    elif matchups[user_choice[0]] == comp_choice[0]:
        print("You win!")

    else:
        print("You lose!")

def main():
    determine_winner(get_user_choice(), get_computer_choice())

if __name__ == "__main__":
    main()
