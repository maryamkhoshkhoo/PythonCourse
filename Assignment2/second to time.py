
time = int(input("Please enter your seconds :"))

hours = int(time // 3600)
minutes = int((time % 3600) // 60)
seconds = int(time % 60)


print ("Time= " ,hours , ":",minutes ,":", seconds)