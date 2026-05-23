# a=input("Enter number1:")
# b=input("Enter number2:")
# print("num 1 is: ",a)
# print("num 2 is: ",b)
# print(a+b)
# # like if i do sum here a=1 b=2 then it should give me 3 but it will
# #  give me 12 because input function takes the value as
# #  string so we have to convert it into integer using int() function   
# #  instead of 3 it give me 12 like it just  place 1 then 2 not add them
# # I have simply used REPL in terminal and this the proof 
# # PS C:\Users\ga> python
# # Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
# # Type "help", "copyright", "credits" or "license" for more information.
# # >>> "Hassan"+"Ali"
# # 'HassanAli'
# # >>> "1" +"2"
# # '12'
# # >>> 1+2
# # 3
# # So I simply have to convert it into integer using int() function like this: that i have learned
# # that we can change the data type of a variable using type casting functions like int(), float(), str() etc.
# a=input("Enter number1:")
# c=int(a) # this will convert the string input into an integer
# e=type(c) # this will give us the data type of variable c proof
# print("Data type of variable c is: ",e)
# b=input("Enter number2:")
# d=int(b) # this will convert the string input into an integer
# f=type(d) # this will give us the data type of variable d proof
# print("Data type of variable d is: ",f)
# print("num 1 is: ",a)
# print("num 2 is: ",b)
# print(c+d)
# so in simple we do 
a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
print("num 1 is: ",a)
print("num 2 is: ",b)
print(a+b)
