#bindal
#python code for dice roll using random python function
import random
min = 1
max = 6

roll_again = "no"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dice again?")
