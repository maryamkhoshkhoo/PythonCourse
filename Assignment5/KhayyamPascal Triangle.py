n = int(input("please enter n:"))

b = [[None for i in range(n)] 
        for j in range(n)]


for i in range(0, n):
    for j in range(0, i+1):
        if(j == 0 or j == i):
            b[i][j] = 1
            print(b[i][j], end = " ")

        else:
            b[i][j] = (b[i -1][j -1] + b[i -1][j])
            print(b[i][j], end = " ")
    print() 