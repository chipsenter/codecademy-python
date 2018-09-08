"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

# User input goes below here >
name = raw_input("Enter a name: ")
user_input1 = raw_input("Pls enter a word: ")
user_input2 = raw_input("Can you enter one more word: ")
user_input3 = raw_input("Ok, One last word pls: ")
# Verbs goes here >
verbs = raw_input("Can you pls enter a verb for me: ")
# Nouns goes here >
noun1 = raw_input("Pls, enter a noun for me: ")
noun2 = raw_input("Pls, enter another noun for me: ")


print 'Mad Libs is starting ...Loading...Loading...Go'

animal = raw_input("Enter: An animal ")
food = raw_input("Enter: A food ")
fruit = raw_input("Enter: A fruit ")
superhero = raw_input("Enter: A superhero ")
country = raw_input("Enter: A country ")
dessert = raw_input("Enter: A dessert ")
year = raw_input("Enter: A year ")

print STORY % (name, user_input1, user_input2, animal, food, verbs, noun1, fruit, user_input3, name, superhero, name, country, name, dessert, name, year, noun2 )