# 1. Arithmetic operators: +, -, *, / etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc.
# 4. Logical operators: and, or, not.

# Arithmetic operators
# 7+5=12
# here 7 and 5 are operands,+ is an operator, 12 is result
_a=12
b_a=12
c=12
c+=_a+b_a # assingment operator is +=
print(c)

# Assignemt operators
# like i have done c=12,c+=_a+b_a(basically adding a b plus c 
# and storing in c)
# if we do increment like by 2
z=4
z+=2
# decrement z by 3
print (z)
z-=3
print (z)
# multiply by 3
z*=3
print (z)
# divide by 3
z/=3
print (z)
# Comparison operators 
# their retuen value is always boolean like simple if you are doing 
g=7<=4
print(g)
# you get a false statement 
g=7>=4
print(g)
# now you get a true statment
u=5==5
print(u)
# yes 5 is equal to 5 == checks equality 
i=5!=6
print(i)
# checks not equality like 5 is not equal to 6

# Logical OPERATORS
# e=True or False
# print (e)
# # here e may be true or may be false so it works because we are using
# # or
# e=True and False
# print (e)
# becaus we are using and here e cant be both true and false
# for or Truth Table:
# e=True or False
print("True and False is ", True or False)
print("True and True is ", True or True)
print("False and True is ", False or True)
print("False and False is ", False or False)
# truth for and
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)
# not operator
print(not(True))
print(not(False))
