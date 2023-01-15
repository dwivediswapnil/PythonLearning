l=[1,12,3,4,5,12]
print(l)

#append() adds a single element to the
# end of the list while . extend() 
# can add multiple individual elements
# to the end of the list
l.append(7)
print(l)

#sort
l.sort()
print(l)

#reverse using sort
l.sort(reverse=True)
print(l)

#reverse the list
l.reverse()
print(l)
#returns the index of first occurence.
print(l.index(12))
#count the number of occurences.
print(l.count(12))

# m=l
#or
m=l.copy()
print(m)
m[0]=0
print(m)
print(l)

#inserting values
#here inserting value at index 1
l.insert(1,899)
print(l)

#adding values at the end using "extend"
m=[900,1000,1100]
l.extend(m)
print(l)

#concatenation
k=l+m
print(k)

