import math

a = float(input("please enter first number:"))
b = float(input("please enter second number:"))

op = input("please enter operation:")

if op == "+":
    result = a + b

if op == "-":
    result = a - b 

if op == "*":
    result = a * b

if op == "/":
    if b!=0:
        result = a / b
    else:
        result = "cannot divide by zero"  

if op == "!": 
    result = "factorial(a)= ", math.factorial(a), "factorial(b)= ", math.factorial(b) 

if op == "√":
    result = ("sqrt(a)= ", math.sqrt(a), "sqrt(b)= ", math.sqrt(b)) 

if op == "sin":
    result = "sin(a)= ", math.sin(math.radians(a)), "sin(b)= ", math.sin(math.radians(b))

if op == "cos":
    result = "cos(a)= ", math.cos(math.radians(a)), "cos(b)= ", math.cos(math.radians(b))

if op == "tan":
    result = "tan(a)= ", math.tan(math.radians(a)), "tan(b)= ", math.tan(math.radians(b))

if op == "cot":
    result = "cot(a)= ", math.cot(math.radians(a)), "cot(b)= ", math.cot(math.radians(b))           


print(result)               