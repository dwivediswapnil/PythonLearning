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
