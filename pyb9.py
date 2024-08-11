<<<<<<< HEAD
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
def upper(l):
    n=l.split(",")
    list=[]
    for i in n:
        list.append(i.upper())
    return(list)

print(",".join(upper("Hello world")))

=======
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
def upper(l):
    n=l.split(",")
    list=[]
    for i in n:
        list.append(i.upper())
    return(list)

print(",".join(upper("Hello world")))

>>>>>>> 55e4c7e (Initial commit)
