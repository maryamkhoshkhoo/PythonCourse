import math
print("a.(x^2)+b.x+c=0")

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

delta = math.sqrt((b**2) - (4*a*c))

if delta > 0:
    print("First answer:", ((-1*b) + delta) / (2*a))
    print("Second answer:", ((-1*b) - delta) / (2*a))

elif delta == 0:
    print("Asnwer:", (-1*b) / (2*a))

elif delta < 0: 
    print("No Answer!")  