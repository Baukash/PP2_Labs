import math

#1

class First:
    string = ''
    def getString(self):
        self.string = input()
        
    def printString(self):
        print(self.string.upper())
        
        
qwe = First()

qwe.getString()

qwe.printString()

#2

class Shape:
    length = 0
        
    def area(self):
        print(self.length*self.length)
        
class Square(Shape):
    def __init__(self, length):
        self.length=length
        

qwe = Square(5)

qwe.area()

#3

class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length=length
        self.width=width
        
    def area(self):
        print(self.width*self.length)
        
        
qwe = Rectangle(4,2)

qwe.area()

#4

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((abs(self.x - other_point.x))**2 + (abs(self.y - other_point.y))**2)
        return distance

point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show() 

point1.move(3, 5)
point1.show()

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")

#5

class Account:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, money):
        self.balance+=money
        print("On your bank account:", self.balance)
        
    def withdraw(self, money):
        if self.balance>=money:
            self.balance-=money
            print("On your bank account:", self.balance)
        else:
            print("Ya vam zapreshayu")
            
dauren = Account('Dauka', 3000)
print("On your bank account:", dauren.balance)
dauren.deposit(7000)
dauren.withdraw(9000)
dauren.withdraw(1000)
dauren.withdraw(1)
dauren.deposit(50)
dauren.withdraw(51)
dauren.withdraw(49)

#6

def isPrime(num):

    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
        
lst = [1, 3, 4, 6, 10, 11, 15, 17, 19]

new_lst = list(filter(lambda x: (isPrime(x) == True), lst))

print(new_lst)
