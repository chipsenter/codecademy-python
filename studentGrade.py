lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
johan = {
  "name": "Johan",
  "homework": [95.0, 97.0, 95.0, 82.0],
  "quizzes": [90.0, 95.0, 78.0],
  "tests": [100.0, 100.0]
}
heidi = {
  "name": "Tyler",
  "homework": [0.0, 80.0, 75.0, 22.0],
  "quizzes": [0.0, 37.0, 58.0],
  "tests": [34.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

def get_average(student):
  homework = average(student["homework"])
  homework = average(student["quizzes"])
  homework = average(student["tests"])
  return 0.1 * average(student["homework"]) + 0.3 * average(student["quizzes"]) + \
0.6 * average(student["tests"])

def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

def get_letter_grade(score):
  if score >= 90:
    return "(A) Outstanding performance, Congratz!"
  elif score >= 80:
    return "(B) Great job, keep it up!"
  elif score >= 70:
    return "(C) You can do better! "
  elif score >= 60:
    return "(D) This is NOT acceptable! "
  else:
    return "(F) You should be a shamed!"


students = [alice, lloyd, tyler]

print get_class_average(students)
print get_letter_grade(get_class_average(students))
