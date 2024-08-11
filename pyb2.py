# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
def factorial(n):
    fac=1
    if n==0:
        print("Cant Find Factorial of Zero")
    else:
        for i in range(1,n+1):
            fac = fac*i

    return(fac)

num=factorial(8)
print(num)