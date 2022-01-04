name = input("please enter your name:")
family = input("please enter your family:")
x = float(input("please enter your score1:"))
y = float(input("please enter your score2:"))
z = float(input("please enter your score3:"))

average = (x + y + z) / 3

if average >= 17:
    status = "Great"

if 17> average >= 12:
    status = "Normal"

if average <12:
    status = "Fail"    

print(name, family, status)
