n = int(input("please enter n:"))
sequence = []

for i in range(n):

    if (i == 0 or i == 1):
        sequence.append(1)

    

    else:
        sequence.append(sequence[i-1] + sequence[i-2])



print(','.join(list(map(str, sequence))))

