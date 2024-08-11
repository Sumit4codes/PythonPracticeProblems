# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200


print("Enter Your Transactions Here: ")
t=[]
while(1):
    entry=input()
    if (entry==""):
        break
    else:
        a=entry.split()
        t.append(a)

sum=0
for i in t:
    if i[0] == "D":
        sum=sum+int(i[1])
    elif i[0]=="W":
        sum=sum-int(i[1])

print("Total Ammount: ",sum)