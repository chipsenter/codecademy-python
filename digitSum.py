"""Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits. For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. (Assume that the number you are given will always be positive.)

Check the hint if you need help!"""


def digit_sum(num):
  return sum( [ int(char) for char in str(num) ] )

print digit_sum(12345)