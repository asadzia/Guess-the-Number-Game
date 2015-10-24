# a codeSkulptor library. To use in python3, download the library manually
import simplegui    

from random import randrange
import math

secret_number = 0
range_number = 100
num_of_guesses = 7

# helper function to start and restart the game
def new_game():
    global secret_number, count
    print("New Game. Guess the Number!")
    secret_number = randrange(0, range_number)
    print("The number lies in the range 0 to %d" % range_number)
    count = num_of_guesses
    print("You have %d guesses" % count)

# define event handlers for control panel
def range100():
    global range_number, num_of_guesses
    range_number = 100
    num_of_guesses = 7
    print
    new_game()
    
def range1000():
    global range_number, num_of_guesses
    num_of_guesses = 10
    range_number = 1000
    print
    new_game()

def input_guess(guess):
    global secret_number, count
    # main game logic goes here	
    myGuess = int(guess)
    print("The guess was %d" % myGuess)

    if myGuess > secret_number and count > 0:
        print("Lower")
        count = count - 1
    elif myGuess < secret_number and count > 0:
        print("Higher")
        count = count - 1
    elif myGuess == secret_number and count >= 0:
        print("Correct")
        new_game()
    else:
        print("You are out of guesses. The answer was %d!" % secret_number)
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame
frame.add_input("Enter Guess", input_guess, 100)
frame.add_button("Range is [0,100)", range100, 100)
frame.add_button("Range is [0,1000)", range1000, 100)

# call new_game 
new_game()
frame.start()
