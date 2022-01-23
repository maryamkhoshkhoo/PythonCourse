a = int(input('First number is:'))
b = int(input('Second number is:'))

for i in range(1, min(a, b)+1):
    if (a % i == 0 and b % i == 0):
        bmm = i
        
print("bmm:", bmm)  