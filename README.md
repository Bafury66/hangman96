# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Table of Contents, if the README file is long
- Not applicable
# A description of the project: what it does, the aim of the project, and what you learned
- The project is aim to build a code for classic game Hangman. Project started with some codes which would select ramdom word from a list of words.
- Followed by more codes to ask user to give an input as single letter.
- Code checks if the given input is valid, if it does, proceed to next. Checks include 
    - if given letter is single letter?
    - if given letter is alphabet?
    - if given letter exisit within randomly choosen word?
- Once given input is valid
    - feedback message to user
    - replace the corresponding "_" in the word_guessed list with the letter
    - add given letter to guessed list
    - tells user how many unique letter remaining
- if given letter is not within the word
    - feedback message to user
    - update remaining live(s)
    - add given letter to guessed list
- Codes and logics above are then collected into a Class call Hangman
- Finally project uses a game_play function to create an instance of the Hangman class.
    - This function takes the word_list (list of words) variable.

# Installation instructions

This Hangman game requires no installation, all that is needed is the code or the file contains the code - milestone_5.py.

# Usage instructions

User will have to run Python file directly - This can be done via any IDE that can run Python file, for example VS Code.

# File structure of the project

To run the game, only milestone_5.py is required with help from IDE.

# License information

Users are allowed to do whatever they want with the code (including commercial use) as long as they provide attribution and include the original license in any copies or substantial uses of the work.

# Experience of going through the project
Computer only do what they have been told through the code. In order to achieve the desired result, it is imporatant to throughly think through the logics required in the project.

Once the framework is developed, it becomes easier to fill the code piece by piece.