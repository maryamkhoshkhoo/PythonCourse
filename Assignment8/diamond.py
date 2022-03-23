n = int(input("please enter rows:"))

for i in range(n): #qesmate balaie
    print(" " * (n-i), "*" * (2*i+1))  #tedade setareha fard ast yani 2i+1

for i in range(n-2, -1, -1): #qesmate paieni & -1 step size ast
    print(" " * (n-i), "*" * (2*i+1)) 