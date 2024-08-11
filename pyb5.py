<<<<<<< HEAD
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class inputtoupper(object):
    def __init__(self):
        self.s=""

    def getString(self):
        self.s= str(input("Enter: "))

    def printString(self):
        print(self.s.upper())


i = inputtoupper()
i.getString()
=======
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class inputtoupper(object):
    def __init__(self):
        self.s=""

    def getString(self):
        self.s= str(input("Enter: "))

    def printString(self):
        print(self.s.upper())


i = inputtoupper()
i.getString()
>>>>>>> 55e4c7e (Initial commit)
i.printString()