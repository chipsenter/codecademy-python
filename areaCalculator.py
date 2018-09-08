""" 
The program should do the following:

Prompt the user to select a shape.
Calculate the area of that shape.
Print the area of that shape to the user.
Let's begin! 
"""
print "Program loading......\n" + "Calculator App Started "

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == 'C'.lower():
  radius = float(raw_input("Input radius: "))
  area = 3.14159 * radius**2
  print "The radius is: %f" % area
elif option == 'T'.lower():
  base = float(raw_input("Enter base of your triangle: "))
  height = float(raw_input("Enter height of triangle: "))
  area = 0.5 * base * height
  print "The area of the triangle is: %f" % area
else:
  print "Invalid input , pls try again!"
# Program exiting  
print "The program is exiting! " 