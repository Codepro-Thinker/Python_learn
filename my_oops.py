#  OOPS

# # class :-
# class student:
#     '''This is demo class'''
#     pass
# print(dir(student))
# print(student.__doc__)  # __doc__ is a variable

# class student:
#     '''This is demo class'''
#     x=10
#     y=20
#     def show():
#         print("hello")
# print(student.__dict__)  # __dict__ is a veriable.



# class student:
#     '''This is demo class'''
#     x=10
#     y=20
#     def show():
#         print("hello")
# # print(dir(student))  # __dict__ is a veriable.
# print(id(student))
# obj=student()
# obj1=student
# obj2=student
# obj3=student
# print(id(obj))
# print(id(obj1))
# print(id(obj2))
# print(id(obj3))

#  OOPS

# class :-
# class student:
#     '''This is demo class'''
#     pass
# print(dir(student))
# print(student.__doc__)  # __doc__ is a variable

# class student:
#     '''This is demo class'''
#     x=10
#     y=20
#     def show():
#         print("hello")
# print(student.__dict__)  # __dict__ is a veriable.





'''class student:
    def __init__(self):   # self :- self is a referance variable that can hold address of current object.
        print("constructer called")
        print(id(self))
obj1=student     # it's called internal constructor.
# print(id(obj1))
obj2=student()  # it's called external constructor.
print(id(obj2),id(student))'''
# self :- self is a referance variable that can hold address of current object.

# WAP to create a external construction code.
'''class student:
    def __init__(self):
        print("constructer called")
        print(id(self))
obj=student
obj1=student()   #  () it is responsive to called external construction.
# print(id(obj),id(obj1))
obj1.__init__()'''


#  WAP to Create a Multiple constructor
'''class student:
    def __init__(self):
        print("constructer called")
        print(id(self))
    def __init__(self):
        print("hiiiii")
obj=student
obj1=student()    # call only last constructor.
obj1.__init__()'''

# WAP to call using internal constructor and class name.
'''class student:
    school='SHSS'
    school_city='Bhopal'
    def detail(self):   # that method it's first parameter is self is called instance method.
        print("from studend class")
obj=student()
print(obj.school,student.school)
print(obj.school_city,student.school_city)
obj.detail()
# student.detail()'''


'''class student:
    def __init__(self,name,age,grade):
        self.n=name
        self.a=age
        self.g=grade
    def display(self):
        print(self.n,self.a,self.g)

obj=student('Shubham',19,'B.Tech')
# obj.display()
print(obj.n,obj.a,obj.g)
# student.display()
# student().display()
# student('Rohit',24,'BSC').display()'''



#    Variables :-

# instance variablr :- change the value to goo obj1 to obj2 is called instance variable.
#                      that method there first parameter is self is also called instance variable.
# declaration  -->  1. In-side class.
#                       (i). In-side constructor.
#                       (ii). In-side instance method
#                   2. out side class.
# calling :-  1. In-side class.
#                (i). In-side constructor.
#                (ii). In-side instance method
#             2. Out-side method

#   Example :- 
 
'''class student:
    def __init__(self,name,contact):
        self.n=name                # declaration in-side constructor
        self.c=contact             # declaration In-side constructor
        print(self.n,self.c)       # calling In-side constructor
    def add_new(self,roll_no):
        self.r=roll_no             # Declaration IN-side instance method
    def display(self):
        print(self.n,self.c,self.r,self.email)  # calling In-side instance method
obj=student('Shubham',32578512)
obj.add_new(101)
# obj.display()                            # AttributeError: 'student' object has no attribute 'email'
obj.email='shubhamnarware45@gmail.com'   # Declaration Out-side of the class
obj.display()
print(obj.n,obj.c,obj.r,obj.email)       # calling  Out-side of the class

print(obj.n)
obj=student('Sahil',3255712)
print(obj.n)'''



# class variable :- it's depends on class.
#  Class variable :-
#  Declaration :- 1. In-side class
#                     (i) In-side constructor
#                     (ii) In-side instance method
#                     (iii) In-side classmethod
#                 2. Out-side of the class

# Calling ;- 1. In-side class
#                (i) In-side constructor
#                (ii) In-side instance method
#                (iii) In-side classmethod
#            2.  Out-side of the class


# Note :- class kee name see hii decaraler hoga or call hoga means class dependent variable
'''class student:
    school_name='SHSS'
    def __init__(self,name,roll_no):
        self.n=name
        self.r=roll_no
        student.school_city='Bhopal'
        print(student.school_city,student.school_name)
    def add_new(self):
        student.school_code=101
        print(student.school_city,student.school_name,student.school_code,student.contact)


student.contact=1234569874
obj=student('Shubham',154)
obj.add_new()
print(student.school_city,student.school_name,student.school_code,student.contact)
# print(obj.school_city)'''

#  Local variable :- 

'''class student:
    def __init__(self):
        x=10              # local variable
        print(x)
    def new(self):
        y=20             # local variable
        z=y+10
        print(z)
        # print(x)
obj=student()
obj.new()'''

#                 CLASS METHOD

'''
class student:
    grade='10th'
    def _init_(self,name,roll_no):
        self.n=name
        self.r=roll_no
    @classmethod
    def update(cls,new):
        cls.grade=new
    @classmethod
    def add_new(cls,add):
        cls.code=add
obj1=student("Naveen","0127cd231323")
print(student.grade)
obj1.update('12th')
print(student.grade)
obj1.add_new("1232234")
print(student.code)
print(obj1.n)
'''

#                 STATIC METHOD

'''class student:
    def _init_(self,roll):
        self.n=roll
    @staticmethod
    def greet(name):
        print(f'welcome {name} to my web page')
obj=student("naveen")
x=obj.n
obj.greet(x)  '''    


# Abstraction   for DATA protection
#            - abstract Class
#            - abstract Method
#            - Concret Method

# Encaptultion for DATA protection
#            - Public Variable/Method
#            - Private Variable/Method
#            - Protected Variable/Method

# Inheritance for Code Reusable
#            - Types
#            - Method overriding
#            - MRO (Method Resolution Order)
#            - Super()

# Polymorphism for Code Reusable
#            - Types - Compile time , Runtime
#            - Overload



#  Inheritance :- There are 5 types of Inheritance-
#   1. Single Inheritance :- Parant --> child
# Example :- 
'''class parent:
    x=10
    def home(self):
        print("from parent class")
class child(parent):
    pass
obj=child()
print(obj.x)
obj.home()'''

# Example of method overriding
'''class parent:
    x=10
    def home(self):
        print("home from parent")
class child(parent):
    def home(self):
        print("home from child")
        super().home()
obj=child()
obj.home()'''

#     2. Multi-level Inheritance :- Grand_parent --> parent --> child
# Example :- 
'''class Grand_parent:
    def home(self):
        print("Home from Grand parent")
class parent(Grand_parent):
    def home(self):
        print("Home from Parent")
        super().home()
class child(parent):
    def home(self):
        print("Home from Child")
        super().home()
obj=child()
obj.home()'''


#   3. Multiple Inheritance :- 
# Example :-
'''class father:
    def home(self):
        print("Home from Father")
        # mother().home()             # provde the access of mother class
        mother.home(self)
class mother:
    def home(self):
        print("Home from mother")
class child(father,mother):           # MRO :- Method Resolution Order
    def home(self):
        print("Home from child")
        super().home()
obj=child()
obj.home()'''



#       4. Hierarchical Inheritance :-
'''class A:
    def home(self):
        print("From class A")

class B(A):
    def home(self):
        print("From class B")
        super().home()   # Will call C.home() next (via MRO)

class C(A):
    def home(self):
        print("From class C")
        super().home()   # Calls A.home()

class D(B, C):
    pass

obj = D()
obj.home()
# obj1=B()
# obj1.home()'''

#                       5. Hybrid Inheritance :- 
