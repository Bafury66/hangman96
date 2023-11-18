import random

class Hangman:
    '''
    This class is used to represent a game of Hangman.
    
    Attributes:
        word_list: a list of words to be used in the game.
        word: randonly choosen from word_list.
        num_lives: number of remaining lives play has, set to 5 initially.
        word_guessed: a list to show play graphically which letter in word is still to be guessed or already guessed.
        num_letters: the number of letters of the word.
        list_of_guesses: a list contains letters player already guessed, set to empty initially.
    '''
    def __init__(self, word_list , num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        print(self.word)
        self.word_guessed = ["_"] * len(self.word)
        print(self.word_guessed)
        self.num_letters = len(set(self.word))
        print(f'Number of UNIQUE letters not been guessed yet = {self.num_letters}')
        self.num_lives = num_lives
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        """
        This function checks if the given letter is within the word to be guessed.
        This feedback player the result of the check.
        If user guesses the wrong letter, function also feedback remaining live(s).
        Args: 
            guess: the letter input from player
        """
        guess = guess.lower() #Convert the guessed letter to lower case
        guess_in_word = False
        for character in self.word: #if statement that checks if the guess is in the word
            if guess == character:
                guess_in_word = True
                break

        if guess_in_word == True: #"When guess is in word, print "Good guess! {guess} is in the word."
            print(f'Good guess! "{guess}" is in the word.')
            # TODO :after print statement, add for-loop to replace word_guessed list
            for index , letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = guess
            print(self.word_guessed)
            self.num_letters -= 1
            print(f'Number of UNIQUE letters remaining = {self.num_letters}')
        else:
            self.num_lives -= 1
            print(f'Sorry, "{guess}" is not in the word.')
            print(f'You have {self.num_lives} lives left.') 
    
    def ask_for_input(self):
        """
        This function ask user for an input in the form of single alphabet.
        Function checks if the given letter meet criteria as well as whether given letter is already tried in previous guess.
        Once pass all checks, 
        """
        condition_flag = True
        # TODO : while loop to run while condition is True
        while condition_flag == True:
            # TODO : Ask the user to guess a letter and assign this to a variable called guess
            guess = input("Please guess and enter a single letter and hit Enter: ")
            # TODO : Create an if statement that runs if the guess is NOT a single alphabetical character
            if len(guess) != 1 and guess.isalpha() != True:
                # TODO : Print the message when condition met
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(f'Here are the letter(s) you have guessed so far: {self.list_of_guesses}')
                print("===="*10)
                return      

def play_game(word_list) -> None:
    """
    This function starts the Hangman game utlising Hangman Class.
    This will not stop until player win the game or lose the game.
    Args: 
        word_list: list of items (in this case fruits) to be randomly choosen
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            #print("Here we go, let's play")
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

word_list = ["apple" , "grape" , "watermelon" , "orange" , "banana" , "strawberry" , "pineapple"]
play_game(word_list)