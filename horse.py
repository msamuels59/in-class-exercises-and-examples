#'''For this exercise, you are going to write a program that models the 
#basketball shooting game, HORSE.

#First, rename this file to horse.py

#- This game has two players.
#- Players alternate taking shots, and, if they miss, they get a letter.
#- For the purposes of this exercise, it will be random whether a player makes
#or misses a given shot.'''

# Hints for getting started

# What variables will you need for this program? In other words, what values
# do you need to keep track of? 

# What functions will you need? What, if any, input will each function require? 
# What, if any, output will the function return? What, if any side effects will
# the function have? For example, will any values be changed?

# For Round 1, DO NOT WRITE ANY CODE. Use comments and psuedocode to plan out
# what you are going to do. For example, you could do something like:
# def shoot(player):
#   determines whether player makes or misses shot
#   updates players letters if missed

# I will hit up each group individually after round one and get you set for round 2.
import random

player_1 = []
player_2 = []

die=[True,False]
#true is hit, false is miss
horse_list = ['H', 'O', 'R', 'S', 'E']

def game():
    if player_1 == "HORSE" :
        print("Player 2 Wins!")
    elif player_2 == "HORSE" :
        print("Player 1 Wins!")
    else:
        shoot()

#shoot function
def shoot():
    player_1_turn = input("Press enter to shoot")
    shot_outcome = random.choice(die)
    if shot_outcome == True :
        print("Nice Shot!")
    else:
        for index, elem in enumerate(horse_list):
            if(player_1<len(horse_list)-1):
                player_1.append(horse_list[index])
            else:
                player_1.append(elem)
shoot()
print(player_1)

        
        
        

