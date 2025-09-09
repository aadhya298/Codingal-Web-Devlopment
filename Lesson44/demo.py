#TUPLES
tup=(12,18,24,26,30,36,42)
print(tup)
print(type(tup))

print(tup[2])
print(tup[-1])

for i in range(0,len(tup)):
    print(f'The {i} element of tup is {tup[i]}')

# tup[1]=20 :- It is not possible as tuples are immutable

p=(25,89,34,'Aashi','Krish',True,[2,4,6,8],'Hi',(3,6,9,12))
print(p[6])
print(p[8][2])

#SETS
A={1,2,2,3,4,5,5,6,7,8,9}
print(A)
print(len(A))

A.add(10)
print(A)

# print(A[4]) :- It is not possible as sets are inaccessible
B={2,3,4,6,7,11,12}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))