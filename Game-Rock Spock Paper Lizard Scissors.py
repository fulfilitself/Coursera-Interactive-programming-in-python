import random

# helper functions

def name_to_number(name):
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print "Warning! Please enter 'rock', 'Spock', 'paper', 'lizard', or 'scissors!'"
        # Arbitrarily assign number to an outrange number.
        number = 10 
    return number

def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    else:
        name = 'scissors'
    return name
        
###################################################

def rpsls(player_choice): 
    # First part of the fn: Show player's choice and convert it to a number.
    print " "
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)  
    
    # Second part of the fn: Generate computer's number and convert it to a name.
    comp_number = random.randrange(0,5) 
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    
    # Last part of the fn: 
    difference = comp_number - player_number
    
    if difference <= -6:       # If player input is invalid, by def, player_number = 10.
        remainder = 6          # Arbitrarily assign remainder as 6
    # If all inputs are valid
    else:                      
        remainder = difference % 5
    
    # Determine the winner:
    if remainder == 4 or remainder == 3:
        print "Player wins!"
    elif remainder == 1 or remainder == 2:
        print "Computer wins!"
    elif remainder == 0:
        print "Player and computer tie!"
    else:                      # When remainder = 6
        print "No result because of invalid input from player!"
    return remainder       
 
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


