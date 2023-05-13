    # HANGMAN
    #### Video Demo:  https://youtu.be/AginGGZQ_xg
    #### Description:
    I chose the Hangman as it is a classic game that has been entertaining people for generations and I really enjoy playing it. I used Python to program this game, and it is designed as a class called "Hangman". The program starts by taking a list of words as input, and it randomly selects one of them as the word to be guessed.

    The objective of the game is to guess the selected word by suggesting one letter at a time. If the guessed letter is present in the word, it is added to the word's guessed letters. The game continues until the player has guessed all the letters in the word, in which case the player wins. Alternatively, if the player runs out of attempts, the game is over, and the player loses.

    The game begins with a certain number of attempts, which in this implementation is ten. If the player guesses a letter that is not in the selected word, the number of attempts is decremented. However, if the player guesses a letter that has already been guessed, the program will remind the player that they have already guessed that letter.

    To make the game more fun and interactive, the program includes a display_word method. This method shows the letters guessed so far and underscores for the remaining letters, making it easier for the player to guess the word. Additionally, the program includes messages to inform the player if they guessed correctly or incorrectly, making the game more engaging and exciting.

    Overall, this implementation of Hangman using Python is an entertaining way to spend your free time. Whether you are an avid Python programmer or just looking for a fun game to play, this implementation is sure to provide you with hours of entertainment. So, why not give it a try and see if you can guess the word before the number of attempts run out?