"""Passing a range into a function
Okay! Range time. The Python range() function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.

range(6) # => [0, 1, 2, 3, 4, 5]
range(1, 6) # => [1, 2, 3, 4, 5]
range(1, 6, 3) # => [1, 4]
The range function has three different versions:

range(stop)
range(start, stop)
range(start, stop, step)
In all cases, the range() function returns a list of numbers from start up to (but not including) stop. Each item increases by step.

If omitted, start defaults to 0 and step defaults to 1."""


def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print my_function(range(0, 3)) # Add your range between the parentheses!