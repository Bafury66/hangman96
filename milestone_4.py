import random

class Hangman:
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
        guess = guess.lower() #Convert the guessed letter to lower case
        guess_in_word = False
        for character in self.word: #if statement that checks if the guess is in the word
            if guess == character:
                guess_in_word = True
                break

        if guess_in_word == True: #"When guess is in word, print "Good guess! {guess} is in the word."
            print(f'Good guess! "{guess}" is in the word.')
        #else:
        #    print(f'Sorry, "{guess}" is not in the word. Try again.') 
    
    def ask_for_input(self):
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
                print(self.list_of_guesses)
                return      

game_list = ["apple" , "grape" , "watermelon" , "orange" , "banana" , "strawberry" , "pieapple"]
game = Hangman(game_list).ask_for_input()
#Hangman.ask_for_input()