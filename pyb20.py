<<<<<<< HEAD
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class DivisibleBySeven:
    def __init__(self,n):
        self.n=n

    def value_generator(self):
        for i in range (1,self.n+1):
            if i%7 ==0:
                yield i

values=DivisibleBySeven(n=100)
for i in (values.value_generator()):
    print(i)
=======
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class DivisibleBySeven:
    def __init__(self,n):
        self.n=n

    def value_generator(self):
        for i in range (1,self.n+1):
            if i%7 ==0:
                yield i

values=DivisibleBySeven(n=100)
for i in (values.value_generator()):
    print(i)
>>>>>>> 55e4c7e (Initial commit)
print(values)