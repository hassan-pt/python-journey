# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 
# here it is listing all the files in c file 
import os

# specify the directory path (you can change this)
path = "/"

# get list of contents
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)

# if i ask from it what's inside my new folder thats in C
path = "/New folder"

# get list of contents
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)