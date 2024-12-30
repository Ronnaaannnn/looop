"""Python program to check the validity of username and password input by users"""
for i in range (1,4):
    a=input("input uid ")
    b=input("enter passord")
    if a != "jello" or b != "hellopy":  
        print("you have ",3-i ,"attempts")
    else:
        print("you logged in")
        break
else :
    print (" you are blocked in")