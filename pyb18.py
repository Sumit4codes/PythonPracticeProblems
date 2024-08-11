# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

def isMin(a):
    if  len(a)>=6:
        return True
    
def isMax(b):
    if len(b)<=12:
        return True
    
def isSmallLetter(c):
    count=0
    for i in c:
        if i.islower():
            count=count+1
    if count > 0:
        return True
    
def isBigLetter(d):
    count = 0
    for i in d:
        if i.isupper():
            count = count + 1
    if count >0:
        return True
    
def isNum(e):
    count=0
    for i in e:
        if i.isdigit():
            count=count+1
    if count>0:
        return True
    

def isChar(f):
    ch=["$","#","@"]
    for i in f:
        if i in ch:
            return True


valid=[]
input= "ABd1234@1,a F1#,2w3E*,2We3345"
l=input.split(",")
for i in l:
    if (isMin(i) and isMax(i) and isChar(i) and isSmallLetter(i) and isBigLetter(i) and isNum(i) ):
        valid.append(i)

print(",".join(valid))