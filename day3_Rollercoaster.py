print("Welcome to the Rollercoaster!")
height = int(input("What is Your Height in cm? "))
if height>=120:
    print("You are Eligible to ride ! Happy Riding and Enjoy")
    age = int(input("What is Your Age? "))
    if age<=12:
        print("Please pay 5$ ")
    elif age<=18:
        print("Please pay 8$ ")   
    else:
        print("Please pay 12$")     
else:
    print("Grow Taller first sorry !")    