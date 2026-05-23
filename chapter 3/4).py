#Slicing with Skip value# we can also use skip value in slicing
# syntax is [start:stop:step]
# step is the skip value which tells how many values to skip after taking one value
# for example if we have a string '0123456789' and we want to get the 
# values from index 1 to 6 but we want to skip every 2 values 
# then we can use the following code
a='0123456789'
print(a[1:7])
print(a[1:7:3])
# here we simply gets first [1:7]
#means 123456 ok now
#:3 means skip two values get 3rd value
# like 1st value taken 2 3 skip then 4 (3rd value taken ) now 5 6 skipped other 
# 3rd value(7)which is taken but no inclued because we have 123456

# another example
b='FazZhendong'
print(b[0:7:2])
# like get first from 0:7 then :2 means get all second values in a linear
# fzhn
# 3rd value is skip value here