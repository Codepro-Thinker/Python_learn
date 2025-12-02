# Decorator :-it is a higher level function to return function.
#             Decorator represent by @

'''def decore(fun_name):
    def inner():
        print('kaa hoo kaisn baa')
    return inner
x=decore(10)        # return inner object function.
print(x)            # given a address of inner value.
x()  '''               # return hello, call inernal function.

# Examaple of Decorator
'''def decore(fun):
    def inner(p,q):
        p=p+5
        q=q*2
        fun(p,q)
    return inner
def add(x,y):
    print(x+y)
res=decore(add)
res(10,20)'''

'''def decore(fun):
    def inner(p,q):
        p=p+5
        q=q*2
        fun(p,q)
    return inner
@decore
def add(x,y):
    print(x+y)
res(10,20)'''

'''def first(fun):
    def inner():
        print('Welcome')
    return inner
@first
def great():
    print("hello")
great()'''

# WAP to check even number
'''n=int(input("Enter any value : "))
def even(n):
    for i in range(1,n+1):
        print(2*i)
even(n)'''

#            Generater 


# GenerTER  Example:-
'''x=range(1,100)
print(list(x))
print(id(list(x)))'''

'''l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i==1 or i==2:
        print(i)
print("hello")
print("brother")
'''

'''def natural_no(n):
    i=1
    while i<=n:
        yield i
        i=i+1
x=10
res=natural_no(x)
print(res)      # o/p --> <generator object natural_no at 0x00000275BF7F2670>
# print(next(res))
# print(next(res))
# print("hello")
# print(next(res))
for _ in range(5):
    print(next(res))
print("hello")
for _ in range(10):
    try:
        print(next(res))
    except StopIteration:
        print("All elements are iteration,i.e. collection is empty")
        break
print("hello")'''

#                 iterable & iterater

# Iterable :- Python collection is called iterable. like, {list,tuple,string,dict}
