#B-11 PRUTHVIRAJ PATIL Set Operations
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}
set2.add(10) #Adding one element to the set
print(set1.union(set2))     #Union of both sets
print(set1.intersection(set2)) #Intersection of both sets
print(set1.difference(set2)) #set1 - set2
print(set2.difference(set1)) #set2 - set1
print(set1.symmetric_difference(set2)) #Symm. Difference of S1 and S2
