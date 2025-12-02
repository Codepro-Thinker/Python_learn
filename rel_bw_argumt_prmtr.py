# Relation b/w argument & parameter :- 

# 1. Positional arguments.
# 2. 


# 1. Positional arguments :- Syntex --> def fun_name(n0. of parameter):
#                                               body...
#                                       fun_name(no. of arguments passed)
#  Total no. of parapmeter= total on. of arguments.

'''def add(x,y,z):
    return x+y+z
p,q,r=10,30,20
res=add(p,q,r)
# res=add(int(input("Enter 1 value : ")),int(input("Enter 2 value : ")),int(input("Enter 3 value : ")))
# print(res)         # o/p --> 60
# res=add()          # TypeError: add() missing 3 required positional arguments: 'x', 'y', and 'z'  
# res=add(p)         # TypeError: add() missing 2 required positional arguments: 'y' and 'z'
# res=add(p,q)       # TypeError: add() missing 1 required positional argument: 'z'
# res=add(p,q,r,5)   # TypeError: add() takes 3 positional arguments but 4 were given
print(res)'''
    

# 2. Default positional argument :-  Syntrx -->  def fuhn_name(parameter with default value):
#                                                        body...
#                                                fun_name(argument is optional)

'''def add(x=0,y=0,z=0,):
    return x+y+z
# res=add()             # o/p --> 0
# res=add(10)           # o/p --> 10
# res=add(10,20)        # o/p --> 30
# res=add(10,20,30)     # o/p --> 60
# res=add(10,20,30,40)  # TypeError: add() takes from 0 to 3 positional arguments but 4 were given
print(res)'''


# 3. Variable length positional argument :-  Syntex --> dfe fun_name(*arguments):
#                                                            body....
#                                                       fun_name(variable-langth arguments)

# Ex. -->
'''def add(*args):
    print(args)
    print(type(args))
add(1,2,3,4,5,6,7,8,9,10)'''

# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
# x=add(1,2,3,4,5)   # o/p --> 15
# print(x)

'''def add(*n):
    sum=0
    for i in n:
        for j in i:
            sum=sum+j
    return sum
x=add(eval(input("Enter any value : ")))
print(x)'''

# def add(*n):
#     print(n)
#     print(type(n))
# x=add(*eval(input("Enter any value : ")))
# print(x)


#  It's remove a tuple returndency -->
'''def add(*n):
    sum=0
    for i in n:
            sum=sum+i
    return sum
x=add(*eval(input("Enter any value : ")))
print(x)'''


# 4.Key-word arguments  :- Syntex --> def fun-name{(x,y,z)  {parameter as a keyword{}
#                                                 print(z)
#                                                 print(x)
#                                                 print(y)
#                                     fun(z=q,y=p,x=s)
'''def fun(x,y,z) :
    print(z)
    print(x)
    print(y)
p=int(input("enter any value : "))
q=int(input("enter any value : "))
s=int(input("enter any value : "))
fun(z=q,y=p,x=s)'''


# 5.Default Key-word arguments :-  Syntex-->
'''def fun(x,y,z) :
    print(z)
    print(x)
    print(y)
p=int(input("enter any value : "))
q=int(input("enter any value : "))
s=int(input("enter any value : "))
# fun(z=q,y=p,x=s)
# fun()
# fun(z=p)
fun(x=q,z=q)'''


# 6.Variable-length Key-word :- Syntex -->
'''def fun_name(**kword):
    print(kword)
    print(type(kword))
fun_name(x=10,y=20,z=30,a=50)'''  

# To findout keys-values and both of given dict :-

'''def fun_name(**kword):
    # for i in kword.keys():  # findout kyes given dict
    #     print(i)
    # for i in kword.values():   # findout valules given dict
    #     print(i)
    for i,j in  kword.items():   # finfout key-value both of then given dict
        print('key = ',i,"value = ",j)
fun_name(**eval(input("enter any dict : ")))'''

# WAP to use all of relational arguments :- 
'''def fun_name(x,y=0,*z,p,**q):
    print(x)
    print(y)
    print(z)
    print(p)
    print(q)
fun_name(10,20,30,40,50,p=25,r=6,s=85,t=99)'''