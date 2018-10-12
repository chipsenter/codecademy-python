"""On line 18, define a new function called grades_variance that accepts one argument, scores, a list.

First, create a variable average and store the result of calling grades_average(scores).

Next, create another variable variance and set it to zero. We will use this as a rolling sum.

for each score in scores: Compute its squared difference: (average - score) ** 2 and add that to variance.

Divide the total variance by the number of scores.

Then, return that result.

Finally, after your function code, print grades_variance(grades)."""



grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  return variance / len(scores)
  
print(grades_variance(grades))  

