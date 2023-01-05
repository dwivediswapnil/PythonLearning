#This is similar to switch case from Java
#break statement is not required here.
x= int(input("Enter the value of x: "))
#x is the variable to match
match x:
    #if x is 0
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case _ if x!=90:
        print("x is ",x)
    case _ if x!=80:
        print("x is ",x)          
    case _:#default case
        print("x is ",x)       