import random
from words import words
import string


def vaild_word(words):
    word = random.choice(words) #choose word from list
    return word.upper()

def guess():
    word = vaild_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        #Letters used
        #joins letters in string separated by space
        print('You have used these letters: ', ' '.join(used_letters))

        #what the current word is 
        word_list = [letter if letter in used_letters else '-' for letter in word]
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


guess()




