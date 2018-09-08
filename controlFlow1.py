def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    elif answer == "up" or answer == "u":
        print "This is the room for the people who believes in fairytales!" 
    elif answer == "down" or answer == "d":
        print "You just entered the room for the badass peoples!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()