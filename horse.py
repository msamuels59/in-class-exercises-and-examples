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


die=[True,False]
#true is hit, false is miss
horse_list = ['no letters','H', 'HO', 'HOR', 'HORS', 'HORSE']

#shoot function
def game():
    player_1 = 0
    player_2 = 0
    for i in range(100) :
            player_1_turn = input("Press enter to shoot, you have " + horse_list[player_1])
            shot_outcome = random.choice(die)
            if shot_outcome == True :
                print("Nice Shot!")
            else:
                if player_1 < 5 :
                    player_1 += 1
                    print("You have " + horse_list[player_1])
                else:
                    print("You have HORSE, Player 2 Wins")
                    break
            player_2_turn = input("Press enter to shoot, you have " + horse_list[player_2])
            shot_outcome = random.choice(die)
            if shot_outcome == True :
                print("Nice Shot!")
            else:
                if player_2 < 5 :
                    player_2 += 1
                    print("You have " + horse_list[player_2])
                else:
                    print("You have HORSE, Player 1 Wins!")
                    break
        
game()
        

