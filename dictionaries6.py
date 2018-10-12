"""ADVANCED TOPICS IN PYTHON
keys() and values()
While .items() returns an array of tuples with each tuple consisting of a key/value pair from the dictionary:

The .keys() method returns a list of the dictionary's keys, and
The .values() method returns a list of the dictionary's values.
Again, these methods will not return the keys or values from the dictionary in any specific order.

You can think of a tuple as an immutable (that is, unchangeable) list. Tuples are surrounded by ()s and can contain any data type.

The 'in' Operator
For iterating over lists, tuples, dictionaries, and strings, Python also includes a special keyword: in. You can use in very intuitively, like so:

"""



my_dict = {
  "Brand": "Kawasaki",
  "Engine": 450,
  "Color": "Green"
}

print my_dict.keys()
print my_dict.values()

for key in my_dict:
  print key, my_dict[key]