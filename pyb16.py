<<<<<<< HEAD
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

n="1,2,3,4,5,6,7,8,9"
ans=[]
l=n.split(",")
for i in l:
    if int(i)%2!=0:
        ans.append(i)

=======
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

n="1,2,3,4,5,6,7,8,9"
ans=[]
l=n.split(",")
for i in l:
    if int(i)%2!=0:
        ans.append(i)

>>>>>>> 55e4c7e (Initial commit)
print(",".join(ans))