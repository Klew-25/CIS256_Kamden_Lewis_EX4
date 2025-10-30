from guess_the_word import get_random_word, process_guess

# Defines a test function for get_random_word
def test_get_random_word():
    word_list = ["lantern", "crisp", "meadow", "fragment", "orbit",
                 "velvet", "anchor", "ripple", "canyon", "ember"]

    result = get_random_word()
    assert result in word_list

# Defines a test function for process_word
def test_process_guess():

    # Pre-determined word by me for easier testing
    random_word = list("test")
    guess_list = [" "] * len(random_word)
    # Pre-determined guess that is for sure in the word
    guess = "e"

    assert process_guess(random_word, guess_list, guess) == True
    # A guess that is for sure not in the word
    guess = "z"
    assert process_guess(random_word, guess_list, guess) == False
