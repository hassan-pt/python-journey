#methods of tuples
a=(90.8,'jkl',98,True,3,4,5,6)
print(a)
print(len(a))#returns the number of items in a tuple
print(type(a))
print(a[0])
print(a.count(3))#returns the number of times a specified value occurs in a tuple
print(a.index(3))#returns the index of the first occurrence of the specified value
t = (1, 2, 3)

print(len(t))   # length
print(max(t))   # largest
print(min(t))   # smallest
print(sum(t))   # sum (numbers only)
# if i want to join two tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)  # (1, 2, 3, 4, 5, 6) 
#merging tuples
a = (1, 2)
b = (3, 4)
c = (5, 6)

result = a + b + c
print(result)
#repitition of tuples
t = (1, 2)
print(t * 3)   # (1, 2, 1, 2, 1, 2)
# here we cannot change the value of a tuple as it is immutable
#  but we can create a new tuple by concatenating the existing tuple with a new value
t1 = t1 + (4,)
print(t1)   # (1, 2, 3, 4)
#check if an element exists in a tuple
t = (1, 2, 3)
print(2 in t)   # True
print(4 in t)   # False
#unpaking a tuple
t = (1, 2, 3)
a, b, c = t
print(a, b, c)   # 1 2 3
print(a)   # 1
print(b)   # 2
print(c)   # 3
