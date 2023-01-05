a=int(input("Enter your age"))
print("Your age is: ",a)

#Conditional operators
# >,<,>=,<=,==
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)

if(a>18):
    print("you can drive")
else:
    print("you cannot driver")    
print("Yay!, your wish.")    # this will act as a finally block because of indentation.

#nested if
num=int(input("Enter the number"))
if(num<0):
    print("Number is negative")
elif(num>0):
    if(num>0 and num<10):
        print("Number is single digit")
    else:
        print("Number is double digit")
else:
    print("Number is Zero , that's it")            
