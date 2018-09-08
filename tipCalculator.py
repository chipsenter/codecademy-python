meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100
print tip, tax
meal += meal * tax
print 'This is meal incl tax ' + str(meal)
total = meal + meal * tip
print 'Your total will be $' + str(float(str(round(total, 2)))) 