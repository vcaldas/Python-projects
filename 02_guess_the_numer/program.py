# Hello world APP - Course Python Jumpstart
# Author: Victor Caldas

import random

print('////////////////////////////////')
print('//   GUEST THE NUMBER GAME    //')
print('////////////////////////////////')
print()

user_name = input("Enter your name: ")
the_number = random.randint(0, 100)
guess = -1
trials = 0

while guess != the_number:
    input_guess = input ("Guess a number between 0 and 100: ")
    guess = int(input_guess)
    trials += 1

    if guess < the_number:
        print("Sorry {0} Your guess of {1} is too low!".format(user_name, input_guess))
    elif guess > the_number:
        print ("Sorry {0} Your guess of {1} is too high!".format(user_name, input_guess))
    else:
        print("You win!")

print("Done! Took you {0} trials, {1}. Bet you can do better next time!".format(trials, user_name))