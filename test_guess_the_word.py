from guess_the_word import get_random_word

# Defines a test function for get_random_word
def test_get_random_word():
    word_list = ["lantern", "crisp", "meadow", "fragment", "orbit",
                 "velvet", "anchor", "ripple", "canyon", "ember"]

    result = get_random_word()
    assert result in word_list