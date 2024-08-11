<<<<<<< HEAD
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

s="Select words to get definitions and translations without leaving the page"
l=s.split()
lenghts=[]
for i in l:
    lenghts.append(len(i))

maximum=max(lenghts)
col=[]
for j in l:
    if len(j)==maximum:
        col.append(j)

for k in col:
=======
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

s="Select words to get definitions and translations without leaving the page"
l=s.split()
lenghts=[]
for i in l:
    lenghts.append(len(i))

maximum=max(lenghts)
col=[]
for j in l:
    if len(j)==maximum:
        col.append(j)

for k in col:
>>>>>>> 55e4c7e (Initial commit)
    print(k)