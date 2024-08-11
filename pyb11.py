# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
    

def b2d(b):
    l=list(b)
    for i in range (len(l)):
        l[i]=int(l[i])
    sum=0
    length=len(l)
    for i in l:
        length=length-1
        sum=sum+(i*(2**(length)))
    return(sum)

a="0100,0011,1010,1001"
b=a.split(",")
ans=[]
for i in b:
    if b2d(i)%5 ==0:
        ans.append(i)
print(",".join(ans))


