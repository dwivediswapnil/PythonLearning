def greater(a,b):
    if(a>b):
        print(a,"is greater")
    else:
        print(b,"is greater")    


for i in range(12):
    if(i==3):
        greater(i,5)

#also an example of keyword arguments.
def sum(a, b=4):
    print(a+b)
sum(b=4,a=2)

#Arbitrary arguments
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is : ",sum/len(numbers))
#it will take input as a tuple.

average(2,3,4,5,6,7,8)    

#Keyword arbitrary arguments 
def name(**name):
    print(type(name))
    print("Hello,",name["fname"],name["mname"],name["lname"])

name(mname="Ashok", lname = "Dwivedi", fname="Swapnil")

