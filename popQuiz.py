print 'Welcome to the Pig Latin Translator!'


original = raw_input("Enter a word: ")
# By using .isalpha you can verify that the string is only contains letters.
if len(original) > 0 and original.isalpha():
  print original 
elif " " in original:
  print "Can't have whitspace in the word!"
elif "-" in original:
  print "Not a valid word?"
elif "/" in original:
  print "That's not a word buddy?"
else:
  print "You haven't entered anything?"