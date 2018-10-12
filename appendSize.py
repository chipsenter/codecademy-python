""".
Create a function called append_size that has one parameter named lst.

The function should append all of the numbers between 1 and the size of lst (inclusive) to the end of lst. The function should then return this new list.

For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 1, 2, 3] because the size of lst was originally 3."""


#Write your function here
def append_size(lst):
  to_extend = list(range(1, len(lst) + 1))
  lst.extend(to_extend)
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))