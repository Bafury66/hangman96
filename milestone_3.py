'''
Python code to continuously ask the user for a letter and validate it.


'''
import random
word_list = ["apple" , "grape" , "watermelon" , "orange" , "banana"]
print(word_list)

word = random.choice(word_list)
print(word)
    
condition = True
while condition == True:
    guess = input("Please guess and enter a single letter and hit Enter: ")
    if len(guess) == 1 and guess.isalpha() == True:
        #print("Oh yeah, that's what I need.")
        print(f'You have entered "{guess}".')
        break
    else:
        print(f'Invalid letter "{guess}". Please, enter a single alphabetical character.')

guess_in_word = False
for character in word:
    if guess == character:
        guess_in_word = True
        break


if guess_in_word == True:
    print(f'Good guess! "{guess}" is in the word.')
else:
    print(f'Sorry, "{guess}" is not in the word. Try again.')

        


