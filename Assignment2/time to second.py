times = [int(input("hours:")), int(input("minutes:")), int(input("seconds:")) ]

a = (times[2]) + (times[1]*60) + (times[0]*3600)

print(times[0],":",times[1],":",times[2], "is", a, "seconds") 