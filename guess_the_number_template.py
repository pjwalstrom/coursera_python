# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

allowed_guesses = 0
secret_number = 0
num_range = 100

# helper function to start and restart the game
def new_game():    
    global secret_number, allowed_guesses
    print "\nNew game. Range is from 0 to",num_range
    secret_number = random.randrange(0, num_range) 
    allowed_guesses = int(math.ceil(math.log(num_range + 1, 2)))
    print "Number of remaining guesses is",allowed_guesses        

# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()

def range1000():
    global num_range
    num_range = 1000    
    new_game()
    
def input_guess(guess):
    global allowed_guesses 
    allowed_guesses -= 1
    print "\nGuess was " + guess + "\nNumber of remaining guesses is",allowed_guesses
    num = int(guess)
    if (secret_number == num):
        print "Correct!"
        new_game()
    elif (allowed_guesses == 0):
        print "You ran out of guesses. The number was",secret_number
        new_game()       
    elif (secret_number < num):
        print "Lower!"
    elif (secret_number > num):
        print "Higher!"  
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric