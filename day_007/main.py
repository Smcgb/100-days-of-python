import random
import hangman_words as words
import hangman_art as art

word_list = words.word_list
lives = 6

logo = art.logo
print(logo)

stages = art.stages

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []


while not game_over:

    print(f"****************************<???>/{lives} LIVES LEFT****************************")

    guess_entire_word = input('Would you like to guess a letter or the whole word? Type "letter" "l" or "word" "w": ').lower()
    while guess_entire_word not in ["letter", "l", "word", "w"]:
        guess_entire_word = input('Would you like to guess a letter or the whole word? Type "letter" "l" or "word" "w": ').lower()

    if guess_entire_word == "word" or guess_entire_word == "w":
        guess = input("Guess the word: ").lower()
        if guess == chosen_word:
            game_over = True
            print("****************************YOU WIN****************************")
        else:
            lives -= 1
            print(f"You guessed {guess}, that's not the word. You lose a life.")
            if lives == 0:
                game_over = True
                print(f"***********************YOU LOSE**********************")
                print(f"The word was: {chosen_word}")
        continue

    guess = input("Guess a letter: ").lower()

    guessed = []
    if guess in guessed:
        print(f"You've already guessed {guess}")
    else:
        guessed.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
