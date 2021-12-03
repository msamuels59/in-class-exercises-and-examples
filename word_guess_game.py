import random
import string

#open words.txt create a dictionary with of the words and amount of characters in said words
with open('words.txt', 'r') as f:
    pick_list = [line.strip() for line in f]

#user difficulty selection 
#easy 4-6
#med 6-8
#hard 8+
easy_list=[x for x in pick_list if len(x) >= 4 and len(x) <= 6]
med_list=[x for x in pick_list if len(x) >= 6 and len(x) <= 8]
hard_list=[x for x in pick_list if len(x) >= 8]

def diff():
    diff_choice = input("Choose your difficulty: easy, medium, or hard.").lower()
    while diff_choice != 'easy' or 'medium' or 'hard':
        if diff_choice == 'easy':
            word = random.choice(easy_list)
            return word.upper()
        elif diff_choice == 'medium':
            word = random.choice(med_list)
            return word.upper()
        elif diff_choice == 'hard':
            word = random.choice(hard_list)
            return word.upper()
        else:
            print('Invalid selection, try again.')
            diff_choice = input("Choose your difficulty: easy, medium, or hard.").lower()


def guess():
    word = diff()
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
                print(f'Your letter,  {user_letter} is not in the word. You have {lives} lives left.')
        
        elif user_letter in used_letters:
            print('You already guessed that.')
        
        else:
            print('Invalid input, try again.')
    if lives == 0:
        print(f"You Lose!, the word was {word}")
    else:
        print("You guessed the word, you win!")
guess()








