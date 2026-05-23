# # escape sequence characters
# # #if i want to want a newline
# # so 
# a="I'm not bad
# at programming"
# #it will definitely give an error because of the new line in the string
# 1) so we do 
a="I'm not bad\nat programming"
print(a)
#2)we have \t which is used for tab space
b="I'm not bad\tat programming"
print(b)
# 3) if i want double quotes in the string then i can do like this
c='I like \"python\" programming'
print(c)
# but i want single quotes in the str i sont want to do anything
d="I like 'python' programming"
print(d)
# 4) \\ → Prints Backslash
e="c:\\users\\python"
print(e)
#it gives us backslash in the output why we use it
# because if we do like this
# f="c:\users\python"
# 5) Sibngle quote in the string
f='I\'m not bad at programming'
print(f)
# 6) \r → Carriage Return
# it is used to return the cursor to the beginning of the line and overwrite the existing text
g="Hello\rWorld"
print(g)
# means that "Hello" will be overwritten by "World" and the output will be "World".
#7) \b → Backspace
# it is used to remove the previous character in the string
h="Hello\bWorld"
print(h)