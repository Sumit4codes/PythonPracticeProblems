<<<<<<< HEAD
#  Write a method which can calculate square value of number

class Square:
    def __init__(self,n):
        self.n=n

    def num(self):
        return(self.n**2)
    

sqr=Square(int(input("Enter the Number to be Squared: ")))
=======
#  Write a method which can calculate square value of number

class Square:
    def __init__(self,n):
        self.n=n

    def num(self):
        return(self.n**2)
    

sqr=Square(int(input("Enter the Number to be Squared: ")))
>>>>>>> 55e4c7e (Initial commit)
print("Ans: ",sqr.num())