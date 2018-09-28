

a = input("Type a number:")
b = input("Type another number:")
#c = input("Type last number:")
a = int(a)
b = int(b)
#c = int(c)
try:
    print(a / b)
except(ZeroDivisionError,ValueError):
    print(" 2nd Number cannot be zero dude!")
