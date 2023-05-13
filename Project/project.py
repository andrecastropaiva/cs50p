import random # imports random module


# creating a new class Hangman
class Hangman:
    # constructor for the Hangman class...takes word as parameter
    def __init__(self, wordslist):
        self.wordslist = wordslist # sets the words attribute to the list of words passed as a argument (see below hangman_list)
        # selects a random word from the list of words and converts it to lowercase... - word is assigned to the generatedword
        self.generatedword = random.choice(wordslist).lower()
        # initialise the word attribute to an empty set for keeping track of the letters guessed so far
        self.word = set()
        # initialising remaining_attempts attribute and set it to 10
        self.remaining_attempts = 10



    # method to display the word in string format
    def display_word(self):
        # using a list comprehension that creates a new list by iterating over the characters in self.generatedword and checking
        # if each character is also in self.word. If it is, the character is added to the new list as is,
        # and if its not an underscore character is added instead.
        # returns a string with the guessed letters of the word and underscores for the remaining letters
        return ''.join(char if char in self.word else '_' for char in self.generatedword)



    # defining a new method that takes letter as argument to keep track of the letters guessed
    # method does not return anything... but updates the instance attributes of the Hangman class... hangman_list
    def guess(self, input_letter):
        # check if the letter has already been guessed
        if input_letter in self.word:
            print('You already guessed that letter.')
        # check if the letter is in the generated word
        elif input_letter in self.generatedword:
            # if it is, add the letter to the set of guessed letters and print a message indicating that the guess was correct
            self.word.add(input_letter)
            print('Correct!')
        else:
            # if the letter is not in the generated word, add it to the set of guessed letters
            self.word.add(input_letter)
            # decrement the number of remaining attempts and print a message indicating that the guess was incorrect
            self.remaining_attempts -= 1
            print('Incorrect. Try again!')




    # game_over method
    def game_over(self):
        # check if the remaining attempts are 0 or if all the letters in the generated word have been guessed
        # it will return false until the attempts reach zero which then prints the game over message OR if the set of character in
        # the player guessed word is a subset of the set of characters in the actual word, in this case prints the congratulations msg
        return self.remaining_attempts == 0 or set(self.generatedword) <= self.word




    def play_game(self):
        # print welcome message
        print('Welcome to Hangman!')
        while not self.game_over():
            # display current state of the word and remaining attempts
            print(f'Word: {self.display_word()} \nAttempts left: {self.remaining_attempts}\n')
            # prompt user to guess a letter and convert to lowercase
            input_letter = input('Guess a letter: ').lower()
            # call guess method to process the guess
            self.guess(input_letter)
        # check if game is over due to running out of attempts
        if self.remaining_attempts == 0:
            print(f'Game over! You ran out of attempts. The word was {self.generatedword}')
        else:
            # game is over due to successfully guessing the word
            print(f'Congratulations! You guessed the word {self.generatedword}. \nThanks for playing Hangman!')





if __name__ == '__main__':
    # create an instance of the Hangman class with a list of words
    hangman_list = Hangman(['dog', 'london', 'python', 'world', 'computer'])

    # start the game by calling the play_game method of the hangman_list object
    hangman_list.play_game()