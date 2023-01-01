a= input("Enter the name:")
print("My name is",a)

x= input("Enter first number: ")
y= input("Enter second number: ")
#By default this input function takes input as string.
print(x+y)

x= int(input("Enter first number: "))
y= int(input("Enter second number: "))
#By default this input function takes input as string.
print(x+y)
#or
# print(int(x)+int(y))

x= int(input("Enter first number: "))
y= input("Enter second number: ")
#By default this input function takes input as string.
print(x+y)
#will result in an type error as we cannot combine number with string.