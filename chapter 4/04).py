#List methods
# in string str functions make new string but
#  in list list_functions make changes in the same list not create new list
#means your original list will be changed by list functions but 
# in string your original string will not be changed by string functions
a=['ali', 98.9, False,5,"Ahmed"]
a.append(90)#append function add new element at the end of the list
print(a)
print(a.pop(2))#it will give that pop element which is removed from the list
a.pop(2)#pop function remove element from the list by index
print(a)
a.insert(3,'Faris')#insert function add new element at the specific index
print(a)
a.reverse()#reverse function reverse the order of the list
print(a)
print(a.index('Faris'))#index function return the index of the first occurrence of the specified element
print(a.count('Faris'))#count function return the number of times the specified element appears in the list
print(a)
a.remove('Faris')#remove function remove the first occurrence of the specified element from the list
print(a)
a.clear()#clear function remove all elements from the list
print(a)
l1=[34,86,35,897,24,]
l1.sort()#sort function sort the list in ascending order 
print(l1)
