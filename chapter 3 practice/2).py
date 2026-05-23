# 2. Write a program to fill in a letter template given below with name and date of user input.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
a=input("Enter your name: ")
b=input("Enter the date: ")
print(letter.replace("<|Name|>",a).replace("<|Date|>",b))
# here i have taken two inputs then using string replace fucntion 
# i have replaced the <|Name|> and <|Date|> with user input.
#first replace function will replace the <|Name|> with user input
#  and then second replace function will replace the <|Date|> with user input.
# if i do individually then it will do like name is replaced and second print date is 
#replaced both printed individually but here i have done in one print statement 
# so it will replace both and print the final output.