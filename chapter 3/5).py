#String Functions
a = "hello World "
print(len(a)) #Length of the string ,we can get length of the string using len() function
print(a.endswith("rld")) #Check if the string ends with given value 
#or not, it returns boolean value
print(a.startswith("he")) #Check if the string starts with given value or not,
#it returns boolean value
print(a.capitalize()) #Convert the first character of the string to upper case
print(a.upper()) #Convert the string to upper case
print(a.lower()) #Convert the string to lower case
print(a.title()) #Convert the first character of each word to upper case
print(a.strip()) #Remove any leading and trailing spaces from the string
print(a.replace("h","n")) #Replace a string with another string
print(a.split(" ")) #Split the string into a list of substrings based on the specified
print(a.split(" ")[0]) #Access the first element of the list returned by split()
print(a.count("o")) #Count the number of occurrences of a substring in the string
print(a.find("o")) #Find the index of the first occurrence of a substring in the