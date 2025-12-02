# map() :- Syntex --> iterable3
#                     iterable2
#                     iterable1
#                     def fun-name(parameter1,parameter2,parameter3):
#                                  body
#                     res=map(fun-name,iterable1,iterable2,iterable3)
#                     print(list(res))

# example question :- 
'''l1=[1,2,3,4,6]
l2=[5,6,7]
l3=[3,2,4,1]
def add(x,y,z):
    return x+y+z
res=map(add,l1,l2,l3)
print(res)              # to show object from result.
print(list(res)) '''       # to display our result.

# WAP to find out squre given number.
'''l=[1,2,3,4]
def squr(n):
    return n**2
res=map(squr,l)
print(tuple(res))'''

# WAP to fint out squre root of given number.
'''l=[1,2,3,25]
def sqrt(n):
    return n**0.5
res=map(sqrt,l)
print(tuple(res))'''

#  Filter() :- Syntex --> iterable   { Note :- only give a single iterable.}
#                         def fun-name(parameter):
#                              body
#                              return
#                         res=filter(fun-name,iterable)
#                         print(list(res))

# Example question :-
'''l=[1,2,3,4,5]
def grater(n):
    if n>=3:
        return n
res=filter(grater,l)
print(list(res))'''

# Reduce :- Syntex --> iterable
#                      def fun-name(parameter1,parameter2):
#                           body
#                      res=reduce(fun-name,iterable)
#                      res=reduce(fun-name,iterable,initial_value)  # optional
#                      print(res)

# Example question.

'''import functools
l=[1,2,3,4,5]
def sum(x,y):
    return x+y
res=functools.reduce(sum,l)
print(res)'''

#WAP to check a max number.
'''from functools import reduce
l=[1,7,3,49,6,5,8]
def maximum(x,y):
    if x>y:
        return x
    else:
        return y
res=reduce(max,l)
print(f' maximum number is : {res}')'''

#WAP to check min number.
'''from functools import reduce
l=[1,7,3,49,6,5,8]
def minimum(x,y):
    if x<y:
        return x
    else:
        return y
res=reduce(max,l)
print(f'Minimum number is : {res}')'''

# WAP to find out sum of squre in given number.
'''from functools import reduce
l=[1,2,3,4,5]
def squre(x,y):
    return x+y**2
res=reduce(squre,l)
print(f'Sum of Squre is : {res}')'''

# WAP to find out the sum of factorial in given number.
'''from functools import reduce
l=[1,2,3,4,5]
def fact(x,y):
    fact=1
    for i in range(1,y+1):
        fact=fact*i
    return x+fact
res=reduce(fact,l)
print(f'Sum of factorial number is : {res}')'''


#                  Lambda function

#  Lambda function :- Syntex --> x= lambda parameters:expression

# Example question :- 
'''x=lambda x,y,z : 2*x+y+z
print(x(1,2,3))'''   # o/p -->7


# Syntex --> lambda x,y : if_result if condition else else_result

'''x=lambda x,y : x if x>y else y
print(x(5,10))'''

# WAP to check a Age.
'''x=lambda age: 'child' if 0<age<18 else('Adult'if 18<age<60 else('Old' if 59<age<100 else 'Invalid value'))
age=int(input("Enter Age : "))
print(x(age))'''

# WAP to check even number using if condition only.
'''x=lambda n: 'even' if n%2==0 else None
n=int(input("Enter and number : "))
print(x(n))'''

# WAP to print squre in  given number.
'''x=lambda n: n**2
n=int(input("Enter any number : "))
print(x(n))'''

# WAP to print n natural number.
'''n=int(input("Enter any number : "))
x=lambda n: [i for i in range(1,n+1)]
print(x(n))'''

# WAP to print n even number.
'''n=int(input("Enter any number : "))
x=lambda n: [i for i in range(1,n+1) if i%2==0]
print(x(n))'''



#  Map with lambda :-

'''l=[1,2,3,4,5]
print(list(map(lambda n:n**2,l)))'''


# WAP to check some operations.
'''l1=[1,2,3,4]
l2=[2,3,4,5]
l3=[6,7,8,9]
print(list(map(lambda x,y,z : x+y+z,l1,l2,l3)))     # sum of given number
print(list(map(lambda x,y,z : x**0.5+y**0.5+z**0.5,l1,l2,l3))) '''    # print squre root for given number

# WAP filter with lambda print even number.
'''l=[1,2,3,4,5,6,7]
print(list(filter(lambda x:'even' if x%2==0 else None,l )))'''
 
# WAP Reduce with lambda print sum of given number.
'''from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7]
total = reduce(lambda x, y: x + y, l)
print(total)'''