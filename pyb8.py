# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def function(w):
    l=w.split(",")
    l.sort()
    return(l)

i= "without,hello,bag,world"
ans= function(i)
print(",".join(ans))