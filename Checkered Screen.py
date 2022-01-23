n = int(input('number of row: '))
m = int(input('number of col: '))

for i in range(n):
    for j in range(m):
        if (i + j)%2 == 0:
            print('#', end=' ')
        else:
            print('*', end=' ')
    print() 