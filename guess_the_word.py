import random

# List of random words
word_list = ["lantern", "crisp", "meadow", "fragment", "orbit",
             "velvet", "anchor", "ripple", "canyon", "ember"]

# Randomly picks a word and turns it into a list
random_word = list(random.choice(word_list))
# Creates an empty list that matches the length of the random word
guess_list = [" "] * len(random_word)
# Establishes guess attempts based on the random word
guess_attempts = len(random_word) + 6

# A loop that runs the game. Will end if user wins or runs out of guesses
while True:
    print(guess_list)
    print(f'Number of guesses left: {guess_attempts}')
    guess = input("Guess a letter: ").lower()
    guess_attempts -= 1

    # Loops through the random word list and adds any matches to the guess list
    for i, letter in enumerate(random_word):
        if letter == guess:
            guess_list[i] = letter

    # Displays if you guess the random word
    if guess_list == random_word:
        print("\nCongratulations! You guessed the word!")
        print(guess_list)
        break

    # Displays if you run out of guess attempts
    if guess_attempts == 0:
        print("\nSorry, you ran out of guesses!")
        break