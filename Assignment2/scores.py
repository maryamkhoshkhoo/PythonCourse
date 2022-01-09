a = int(input("please enter the number of students:"))
scores = []
for i in range(a):
    x = float(input("please enter scores:"))
    scores.append(x)

average = sum(scores) / len(scores) 

print("average=", average, "max=", max(scores), "min=", min(scores))     
