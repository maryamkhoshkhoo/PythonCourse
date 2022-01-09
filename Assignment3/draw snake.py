Length_snake = int(input("n = "))

snake = " " 

for i in range(Length_snake):
    if (i % 2 == 0):
        snake += '*'
    else:
        snake += '#'
        
print(snake) 