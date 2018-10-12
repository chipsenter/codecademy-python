"""Define a function, grades_average, below the grades_sum function that does the following:

Has one argument, grades_input, a list
Calls grades_sum with grades_input
Computes the average of the grades by dividing that sum by float(len(grades_input)).
Returns the average.
Call the newly created grades_average function with the list of grades and print the result."""

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total

print grades_sum(grades)

def grades_average(grades_input):
  average = grades_sum(grades_input) / float(len(grades_input))
  return average
  
  
print(grades_average(grades))