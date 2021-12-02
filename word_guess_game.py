from math import pi
import random

import string

#open words.txt create a dictionary with of the words and amount of characters in said words
with open('words.txt', 'r') as f:
    pick_list = [line.strip() for line in f]

#word_dictionary = {}
#for item in pick_list:
#    word_dictionary.setdefault(len(item), []).append(item)
easy_list=[x for x in pick_list if len(x) >= 4 and len(x) <= 6]
med_list=[x for x in pick_list if len(x) >= 6 and len(x) <= 8]
hard_list=[x for x in pick_list if len(x) >= 8]

def vaild_word(pick_list):
    word = random.choice(pick_list) #choose word from list
    return word.upper()

#user difficulty selection 
#easy 4-6
#med 6-8
#hard 8+



def guess():
    word = vaild_word(pick_list)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 8
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        #Letters used
        #joins letters in string separated by space
        print('You have used these letters: ', ' '.join(used_letters))

        #what the current word is 
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1 
                print('Your letter, ', user_letter, 'is not in the word.')
        
        elif user_letter in used_letters:
            print('You already guessed that.')
        
        else:
            print('Invalid input, try again.')
    if lives == 0:
        print("You Lose!")
    else:
        print("You guessed the word, you win!")
print(hard_list)








