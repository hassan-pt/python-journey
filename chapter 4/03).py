#List slicing
List=[56,True,3.14,"Hello",56,False,'Ali']
# positive_slicing
print(List[2:5])
print(List[:4])
print(List[3:])
print(List[:])
#negative_slicing
print(List[-4:-1])
print(List[-4:])
print(List[:-2])
print(List[-1:])
#step_slicing
#step slicing is used to skip elements in a list while slicing. 
# It takes three parameters: start, stop, and step. 
# The step parameter specifies the number of elements to skip between each element in the slice.
print(List[0:6:2])
print(List[1:6:2])
print(List[::3])#it will print the first element and then skip 
#2 elements and print the next one and so on until the end of the list.
