a = float(input("please enter a:"))
b = float(input("please enter b:"))
c = float(input("please enter c:"))

if a < (b + c) and b < (a + c) and c < (a + b): 
    result = "possible"

else: 
    result = "impossible"  

print(result)    
