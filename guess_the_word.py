import random

# List of random words
word_list = ["lantern", "crisp", "meadow", "fragment", "orbit",
             "velvet", "anchor", "ripple", "canyon", "ember"]

random_word = list(random.choice(word_list))
length = len(random_word)
guess_list = [" "] * length
guess_attempts = len(random_word) + 3

while True:
    print(guess_list)
    print(f'Number of guesses left: {guess_attempts}')
    guess = input("Guess a letter: ").lower()
    guess_attempts -= 1

    for i, letter in enumerate(random_word):
        if letter == guess:
            guess_list[i] = letter

    if guess_list == random_word:
        print("\nYou guessed the word!")
        print(guess_list)
        break

    if guess_attempts == 0:
        print("\nSorry, you ran out of guesses!")
        break