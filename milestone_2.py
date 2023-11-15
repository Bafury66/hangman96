import random
word_list = ["apple" , "grape" , "watermelon" , "orange" , "banana"]
# print(word_list)

def get_random_word() -> None :
    word = random.choice(word_list)
    print(word)
    
def get_single_letter():
    decider = True
    while decider == True:
        guess = input("Please enter a single letter: ")
        #print(f'You have entered " {guess} ".')
        if len(guess) == 1 and guess.isalpha() == True:
            print("Good guess!")
            return guess    
        else:
            print("Oops! That is not a valid input.")
  
    
    
get_random_word()
get_single_letter()
