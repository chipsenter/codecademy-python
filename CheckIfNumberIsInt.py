def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print is_int(7.0)   # True    
print is_int(7.5)   # False    
print is_int(-1)    # True