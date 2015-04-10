# program for "Guess the number" mini-project
import simplegui
import random
import math

secret_number = 0
low = 0             #range parameter--low end
high = 100          #range parameter--high end
remain_guess = 0    

def new_game():
    """helper function to start and restart the game"""
    global secret_number, remain_guess
    secret_number = random.randrange(low, high)        
    remain_guess = int(math.ceil(math.log(high - low + 1.0)/math.log(2.0)))
    print ""
    print "New game. Range is from", low, "to", high
    print "Number of remaining guesses is", remain_guess
    return secret_number

# define event handlers for control panel
def range100():
    """button that changes the range to [0,100) and starts a new game"""
    global high
    high = 100     # redefine range parameter
    new_game()   
    
def range1000():
    """button that changes the range to [0,1000) and starts a new game"""     
    global high
    high = 1000    # redefine range parameter
    new_game()
    
def input_guess(guess):
    """input field that request a player input and yield a result"""
    guess_number = int(guess)            # convert string input to a integer
    global remain_guess 
    remain_guess = remain_guess - 1      # count down number of guesses
    print ""
    print "Guess was", guess_number
    print "Number of remaining guesses is", remain_guess
    if remain_guess == 0:                # if this is the last chance 
        if guess_number == secret_number:# if guess_number is right, player still wins.
            print "Correct!"
            new_game()
        else:                            # if guess_number is wrong, then startover
            print "Out of guesses!"
            new_game()
    else:                                # if not the last chance
        if guess_number < secret_number:     
            print "Higher!"  
        elif guess_number > secret_number:
            print "Lower!"
        else:
            print "Correct!"
            new_game()                      
        
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)                           
f.add_input("Enter a guess", input_guess, 200)

new_game()

#start frame
f.start()
