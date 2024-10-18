import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()

# below is the logic for the game without function code
"""def main():
    while True:
        print(art.logo)
        for i in range(2):
            user_cards.append(random.choice(cards))
            dealer_cards.append(random.choice(cards))

        user_score = sum(user_cards)
        dealer_score = sum(dealer_cards)

        # check for Blackjack at the start of the game
        if user_score == 21:
            print("You win with a Blackjack!")
            keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
            if keep_playing == 'n':
                return False
            else:
                return True
        elif dealer_score == 21:
            print("Dealer wins with a Blackjack!")
            keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
            if keep_playing == 'n':
                return False
            else:
                return True

        # start game
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        # begin hitting or standing

        while True:
            hit_or_stand = input("Type 'hit' to get another card, type 'stand' to pass: ").lower()
            while hit_or_stand not in ['hit', 'stand']:
                hit_or_stand = input("Invalid input. Please try again. Type 'hit' to get another card, type 'stand' to pass: ").lower()

            if hit_or_stand == 'hit':
                user_cards.append(random.choice(cards))
                user_score = sum(user_cards)
                print(f"Your cards: {user_cards}, current score: {user_score}")
                if user_score > 21 and 11 in user_cards:
                    user_cards.remove(11)
                    user_cards.append(1)
                    user_score = sum(user_cards)
                    print(f"Your cards: {user_cards}, current score: {user_score}")
                elif user_score > 21:
                    print(f"Your cards: {user_cards}, current score: {user_score}")
                    print("You went over. You lose.")
                    keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
                    if keep_playing == 'n':
                        return False
                    else:
                        return True
            else:
                break

        # dealer's turn
        print(f"Dealer's cards: {dealer_cards}, current score: {dealer_score}")
        while dealer_score < 17:
            dealer_cards.append(random.choice(cards))
            dealer_score = sum(dealer_cards)
            print(f"Dealer's cards: {dealer_cards}, current score: {dealer_score}")
            if dealer_score > 21 and 11 in dealer_cards:
                dealer_cards.remove(11)
                dealer_cards.append(1)
                dealer_score = sum(dealer_cards)
                print(f"Dealer's cards: {dealer_cards}, current score: {dealer_score}")
            elif dealer_score > 21:
                print(f"Dealer's cards: {dealer_cards}, current score: {dealer_score}")
                print("Dealer went over. You win!")
                keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
                if keep_playing == 'n':
                    return False
                else:
                    return True

        # compare scores
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        if user_score > dealer_score:
            print("You win!")
        elif user_score == dealer_score:
            print("It's a draw.")
        else:
            print("You lose.")
        keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if keep_playing == 'n':
            return False
        else:
            return True"""

if __name__ == "__main__":
    main()