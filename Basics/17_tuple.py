#Tuples are ordered collection of items.
#differnce between list and tuple is 
#that tuple cannot be changed i.e they immutable 

tup=(1,2,3,4,5,True,"ref")
print(type(tup))
print(tup[5])
#We cannot change the value 
# tup[0]=3
# print(tup)
print(tup[-3])#means len(tup)-3 i.e 7-3=4
if 19 in tup:
    print("Yes present")
else:
    print("false") 

#slicing
tup3=tup[1:4]
print(tup3)        
#comma is necessary
tup1=(1,)
print(type(tup1))
print(tup1)

#if given tup[:90], this means tup[0:90]
#if given tup[2:], this means tup[2:len(tup)]

even_num=(2,4,8,6,10,12,14,16,18,20,22,24)
print(even_num[0:8:3])

#methods in tuple 
#to change the content of the tuple , we 
#should firstly change it into list , then 
#change into tuple.
countries=("India","Israel","Australia","Africa","America")
print(countries)
temp=list(countries)
print(temp)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries = tuple(temp)
print(countries)

countries2=("Algeria","Moscow","Iran")
#on concatenation, a new tuple wil be formed
print(countries+countries2)
#count
print(countries2.count("Algeria"))
# to get the first occurence 
res= countries.index("Israel")
print(res)
tuple1=(0,2,3,4,5,6,7,89,5)
#(3,0,3) means that search for 3 between 0
#to <3
res1= tuple1.index(3,0,3)
print(res1)

print(len(tuple1))