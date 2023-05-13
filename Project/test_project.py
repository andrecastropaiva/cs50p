from project import Hangman


def test_display_word():
    # create instance of Hangman class with a known generated word
    hangman_list = Hangman(['python'])
    # set the guessed letters so far to 'pt'
    hangman_list.word = {'p', 't'}
    # check that the display_word() method returns the correct string
    assert hangman_list.display_word() == 'p_t___'




def test_guess():
    # create instance of Hangman class with a known generated word
    hangman_list = Hangman(['python'])
    # guess the letter 'p' which is in the generated word
    hangman_list.guess('p')
    # check that the guessed letters set contains 'p'
    assert 'p' in hangman_list.word
    # check that the remaining attempts is still 10
    assert hangman_list.remaining_attempts == 10
    # guess the letter 'x' which is not in the generated word
    hangman_list.guess('x')
    # check that the guessed letters set contains 'x'
    assert 'x' in hangman_list.word
    # check that the remaining attempts is now 9
    assert hangman_list.remaining_attempts == 9




def test_play_game():
    # create a Hangman instance with a list of words
    hangman_list = Hangman(['cat', 'dog', 'bird'])

    # set the generatedword to 'cat' for testing
    hangman_list.generatedword = 'cat'

    # test game over when attempts reach zero
    hangman_list.remaining_attempts = 0
    assert hangman_list.game_over() == True

    # test game over when word is guessed correctly
    hangman_list.word = set(['c', 'a', 't'])
    assert hangman_list.game_over() == True