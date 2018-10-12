"""Stride Length
A positive stride length traverses the list from left to right, and a negative one traverses the list from right to left.

Further, a stride length of 1 traverses the list "by ones," a stride length of 2 traverses the list "by twos," and so on.
"""

to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens
