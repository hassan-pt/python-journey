#Tuples
#tuple is an imutable data type
#tuples are ordered collection of items
#basically we want to use tuples when we want to store a collection of items that should not be changed
a=(1,2,3,4,5)
print(a)
print(type(a))
#empty tuple
b=()
print(b)
# if i want to create a tuple with one element
c=(1,)# i use comma because if i write c=(1) it will be considered as an integer not a tuple
print(c)
#proof
# c=(1)
# print(type(c))
#so we have to use comma to create a tuple with one element
# e=(123,False,'HKLJ',90.0)
# print(e)
# e[2]=23 # this will give an error because tuples are immutable