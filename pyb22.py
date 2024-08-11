<<<<<<< HEAD
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

s="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
words=s.split()
done=[]
for word in words:
    if word in done:
        continue
    done.append(word)

    count=0
    for j in words:
        if word==j:
            count=count+1
=======
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

s="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
words=s.split()
done=[]
for word in words:
    if word in done:
        continue
    done.append(word)

    count=0
    for j in words:
        if word==j:
            count=count+1
>>>>>>> 55e4c7e (Initial commit)
    print(word +" : " + str(count))