"""The program should do the following:

Roll a pair of dice.
Add the values of the roll.
Ask the user to guess a number.
Compare the user's guess to the total value.
Determine the winner (user or computer).
Let's begin!"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess
  
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is: %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
  	print "Your guess %d is above maximum limit" % guess 
  else:
    print "Rolling..."
    sleep(2)
    print "Computer rolls 1st dice %d " % first_roll
    sleep(1)
    print "Computer rolls 2nd dice %d " % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "The total is %d." % total_roll
    print "Result...."
    sleep(1)
    if guess > total_roll:
    	print "WOW, You won congratz"
    else:
      print "Sorry you lost buddy!"
    
roll_dice(6)
