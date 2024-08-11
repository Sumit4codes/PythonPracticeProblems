<<<<<<< HEAD
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
a=[]
for i in range(1000,3001):
    l=list(str(i))
    length=len(l)
    c=1
    for j in (l):
        if int(j)%2 !=0:
            c=0
            break
    if (c==1):
        a.append(str(i))



=======
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
a=[]
for i in range(1000,3001):
    l=list(str(i))
    length=len(l)
    c=1
    for j in (l):
        if int(j)%2 !=0:
            c=0
            break
    if (c==1):
        a.append(str(i))



>>>>>>> 55e4c7e (Initial commit)
print(",".join(a))