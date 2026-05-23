#Lists
#these are the containers to store a set of values of any data type
#e.g
list=['Apple',56,78.9,'Banana','Hassan',True]
print(list)
print(type(list))
print(list[0]) #to access the first element of the list
print(list[1]) #to access the second element of the list
print(list[2]) #to access the third element of the list 
print(list[3]) #to access the fourth element of the list
print(list[4]) #to access the fifth element of the list
print(list[5]) #to access the sixth element of the list
#list is mutable which means we can change the value of the list
#we can't do this with strings because they are immutable
list[3]='Mango' #changing the value of the fourth element of the list
print(list)
list[2]=False
print(list[2]) #to access the third element of the list after changing its value
# as simply we can change the value of the list we can also add new elements to the list
# we can change any data type of list to any other data type of list