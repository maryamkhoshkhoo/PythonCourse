n = int(input('number of row: '))
m = int(input('number of col: '))

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i*j, end=' ')
    print()           
