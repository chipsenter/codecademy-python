"""CONTROL FLOW
Try and Except Statements
if, elif, and else statements aren't the only way to build a control flow into your program. You can use try and except statements to check for possible errors that a user might encounter.

The general syntax of a try and except statement is

try:
    # some statement
except ErrorName:
    # some statement
First, the statement under try will be executed. If at some point an exception is raised during this execution, such as a NameError or a ValueError and that exception matches the keyword in the except statement, then the try statement will terminate and the except statement will execute.

Let's take a look at this in an application. I want to write a function that takes two numbers, a and b as an input and then returns a divided by b. But, there is a possibility that b is zero, which will cause an error, so I want to include a try and except flow to catch this error.

def divides(a,b):
  try:
    result = a / b
    print (result)
  except ZeroDivisionError:
    print ("Can't divide by zero!")
Now that you see how it works, try to write one yourself."""


def raises_value_error():
  raise ValueError
  
try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")