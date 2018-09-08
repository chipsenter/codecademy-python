pyg = 'ay'

original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
new_word = word + first + pyg 
new_word = new_word[1:len(new_word)]
print new_word

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