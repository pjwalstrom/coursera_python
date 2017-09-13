# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

allowed_guesses = 0
secret_number = 0
num_range = 100

# helper function to start and restart the game
def new_game():    
    print "\nNew game. Range is from 0 to",num_range
    if (num_range == 100):
        range100()
    else:
        range1000()
    print "Number of remaining guesses is",allowed_guesses        

# define event handlers for control panel
def range100():
    global num_range, allowed_guesses
    num_range = 100
    allowed_guesses = 7
    new_game()

def range1000():
    global secret_number, allowed_guesses
    secret_number = random.randrange(0,1000) 
    allowed_guesses = 10
    
def input_guess(guess):
    global allowed_guesses 
    num = int(guess)
    print "\nGuess was",num
    allowed_guesses -= 1
    print "Number of remaining guesses is",allowed_guesses
    if (secret_number > num):
        print "Higher!"
    elif (secret_number < num):
        print "Lower!"
    else:
        print "Correct!"  
        new_game()
    if (allowed_guesses == 0):
        print "You ran out of guesses. The number was",secret_number
        new_game()       
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
