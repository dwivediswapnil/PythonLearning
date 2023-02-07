s1={1,2,3,4,5}
s2={2,3,6,7}
print(s1.union(s2))
s1.update(s2)#will update s1 with the values of s2
print(s1)

a1={1,2,3,4,5}
a2={2,3,4,8,0,8,0,9}
print(a1.intersection(a2))
a1.intersection_update(a2)
print(a1)

a3={1,2,3,4}
a4={23,2,3,9,8}
print(a3.symmetric_difference(a4))#will remove the intersection element.(since AUB-AintersectionB)

print(a3.difference(a4))#prints the values present in a3 but not in a4
print(a3.isdisjoint(a4))#since there are no elements in a3 which are not in a2
print(a3.issuperset(a4))
print(a3.issubset(a4))
a3.add(5)
print(a3)
a3.update({7,8,9,10})#if more than 1 item needs to be added .
print(a3)

a3.remove(10)
print(a3)
a3.discard(2)
a4.pop()
print(a4)#will pop randomly

#del command will delete ex: del a4

#to clear all the items in the set we use set method
a3.clear()
print(a3)
