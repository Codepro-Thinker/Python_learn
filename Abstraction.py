# Abstraction :- 
#                 1. Abstract class
#                 2. Abstract method
#                 3. Concrete method
# Note :- From abc import ABD, abstract_method.It is a abstract baase class.
#         TO make a abstract method using @abstractmethoda top of write a method.

'''from abc import ABC, abstractmethod 
class A(ABC):
    def dashboard(self):
        print("Welcome to Deshboard")
    @abstractmethod
    def login(self):
        pass
class B(A):
    def login(self):
        print("Login Successfully")
obj=B()
obj.dashboard()
obj.login()'''

# Encapsulation :-
#                  Access specifire/ modifier :- It is not acceptable/not recomdable in offical python but, 
#                                                It posible to in someways.
#                                  1. Public --> variable/method (x,add())
#                                  2. protected --> variable/method (_x,_add()) {Not supporteed}
#                                  3. private --> variable/method (__x,__add())

# Public variable & method :-
'''class A:
    x=10
    def show(self):
        print("From class A")
        print(A.x)
class B(A):
    pass
obj=B() 
print(obj.x)
obj.show()
print(A.x)
# print(A.show(10))
A.show(10)'''

# Protected variable & method :-
'''class A:
    _x=10
    def _show(self):
        print("From class A")
        print(A._x)
class B(A):
    pass
obj=B() 
print(obj._x)
obj._show()
print(A._x)      # they are access out of class that's by pyython is not supported.
A._show(10)   
# print(A.show(10))'''


# Private variable & method :-
'''class A:
    __x=10
    def __show(self):
        print("From class A")
        print(A.__x)     # Inside class 
class B(A):
    pass
obj=B() 
# print(obj.__x)      # Through child class not supported error
# obj.__show()        # Through child class not supported
# print(A.__x)        # out side class not supported
# print(A.show(10))   # out side class not supported
# A.__show(10)        # out side class not supported
print(dir(A))
print(A._A__x)'''

# Name Mangle :- Syntex :- __class_name__variable / method


# Polymorphism :-

'''
class Human:
    def sound(self):
        print("Human sound")
class Animal:
    def sound(self):
        print("Aminal sound")
l=[Human(),Animal()]
for i in l:
    i.sound()'''


# Example of polymorphism --> 
'''class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())
print("Area of Triangle:", triangle.area())'''

