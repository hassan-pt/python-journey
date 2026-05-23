# type() function is used to find the data type of a given variable in python
a=10
t=type(a)
print(t)
# it shows it is an integer type of data 
# if we do
b="Hassan"
z=type(b)
print(z)
# it shows it string type data
c=10.9999999
v=type(c)
print(v)
# its a floating data type
# if i want like c data type should be an integer how would i do that
d=10.9999999
p=int(d)
l=type(p)
print(l)
# now this d thta is float its dat type become int
# sting to flaot
n="89.9"
m=float(n)
k=type(m)
print(k)
# it does for float 
# no="89.9"
# mo=int(no)
# ko=type(mo)
# print(ko)
# it doenot do int here because we point float number in string but if we does
no="89"
mo=int(no)
ko=type(mo)
print(ko)
# it does here
#if we have an array want to converto to float it doenot do this
# name="Hassan"
# change=float(name)
# tell=type(change)
# print(tell)
# if we want to convert str to int in memory it doesnot do that also
# name="Hassan"
# change=int(name)
# tell=type(change)
# print(tell)
# str(31) =>"31" # integer to string conversion
# int("32") => 32 # string to integer conversion
# float(32) => 32.0 # integer to float conversion