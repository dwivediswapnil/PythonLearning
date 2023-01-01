#Conversion of one data type to another is type casting.
a='1'#String
b='2'#String
print(a+b)#Summation will be concatenated
print(int(a)+int(b)) #converting the string to integer

# a=1
# b='2'#String
# print(a+b)
#will give Type error

#2 types of typecasting are there 
#1: Explicit: Done by me.
print(int(a)+int(b))

#2: Implicit: Done by python.
#There are levels of datatypes in python.It converts smaller data type to higher data type .
c=1.5 #float
d=9 #int
#since Float>int, so it will be converted to float.
print(c+d)
print( type(c+d))

