# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


c={"DIGIT":0,"LETTER":0}
a= input("Enter here: ")

for i in a:
    if i.isdigit():
        c["DIGIT"]=c["DIGIT"]+1
    elif i.isalpha():
        c["LETTER"]=c["LETTER"]+1

print("LETTER",c["LETTER"])
print("DIGIT",c["DIGIT"])