from register import *


print("welcome to kunal banking project")
while True:
    try:
        register=int(input("1. signup\n"
                           "2. signin"))
        if register== 1 or register == 2:
            if register ==1:
                signup()
            
        else:
            print("please enter valid input from options")

    except ValueError:
        print("invalid input try again with numbers")