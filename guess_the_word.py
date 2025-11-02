import random

# List of random words
word_list = ["lantern", "crisp", "meadow", "fragment", "orbit",
             "velvet", "anchor", "ripple", "canyon", "ember"]

# Function that returns a random word from the word list
def get_random_word():
    return random.choice(word_list)

# Function that mimics the logic of the game so that it can be tested
def process_guess(random_word, guess_list, guess):
    result = False
    for j, element in enumerate(random_word):
        if element == guess:
            guess_list[j] = element
            result = True
    return result

# Runs the current file
if __name__ == "__main__":
    # Randomly picks a word and turns it into a list
    random_word = list(get_random_word())
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

        # Displays a message if the guess was in the word or not
        if guess in random_word:
            print('\nNice, that letter is in the word!')
        else:
            print('\nSorry, that letter is not in the word.')

        # Displays if you guess the random word
        if guess_list == random_word:
            print("\nCongratulations! You guessed the word!")
            print(guess_list)
            break

        # Displays if you run out of guess attempts
        if guess_attempts == 0:
            print("\nSorry, you ran out of guesses!")
            break