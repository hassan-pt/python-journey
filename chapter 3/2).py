#First of all i'll tell that string is immuteable 
#in python which means we can't change the value of a string once it is created.
#e.g we have c="HASSAN "
#if i want to change S with N then i can't do that
# because string is immuteable we cant chnage any portion of the string
# we have to create a new string with the desired changes. 

#String Slicing
#String slicing is a technique used to extract a portion of a string.
#e.g I have a string "HASSAN" the length of this string is 6
#in srting we have indexing each character in a string has an index number starting from 0 to
#n-1 where n is the length of the string.
#e.g H A S S A N ,,,,H=0 A=1 S=2 S=3 A=4 N=5 
# we can do indexing in negative way also in negative indexing we start
# from the end of the string and the index number starts from -1 to
# -n where n is the length of the string. 
#in e.g H A S S A N ,,,,N=-1 A=-2 S=-3 S=-4 A=-5 H=-6

# if i want to get length of string then i can use len() function
a='ALi'
print(len(a))
b=a[0:1]
print(b)
# what i have done here it is slicing to get a short desired string from otiginal how to 
# do that the formula is string_name[start_index:end_index]
# where end index is exclusive which means it will not include the character at end_index
b='HAGHJJHKLK'
print(b[0:7])
# i get short desired string from original string

c='234567890'
print(c[3:5])
#i get 56 here 
# if i want to get just one char then i'll do like
c1=c[4]
print(c1) #i'll get 6 here

"""i do negative indexing also
like"""
w="Ayaan"
print(w[-3:-1]) # here -1 is exclusive so it will not include 
# the character at -1 index which is n