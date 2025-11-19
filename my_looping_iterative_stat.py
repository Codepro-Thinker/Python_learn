# Iterative / Looping Statements :- There are present in two loop.
#                                   1. while loop--> (Infinite iterative)
#                                      a. while-else
#                                   2. for loop --> (Finite iterative)
#                                      a. for-else
#  Syntex of for loop :- for i in iterative: {for body executed when elements exits in iteraive(Str,tuple,list,dic)}

# Example of for loop :- 
  
'''s='python'
for i in s:
    print(i)

l=[1,2,3,4,5,6]
for i in l:
    print(i+5)   

t=(1,2,5,'java')
for i in t:
    print(i)   

d={'s':25,'y':64,'a':97}
for i in d:
    print(i,d[i])   

s={1,2,3,4,5,6}
for i in s:
    print(i)   

s=input("Enter your Name : ")
# v,c=0,0
v=c=0
# s.lower()
for i in s:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        v=v+1
    elif(i==' '):
        pass
    else:
        c=c+1
print(f'con is {c} vobles is {v}')'''

'''s=input('enter any String : ')
s=s.replace('','')
if(s.isalpha()):
    print("Alphabetes")
else:
    print("Not Alphabetes")'''


# Question :- 

'''s=input('enter any String : ')
s=s.replace('','')
v=c=0
if(s.isalpha()):
    s=s.lower()
    for i in s:
        if i in ('a','e','i','o','u'):
            v=v+1
        else:
            c=c+1

    print(f'Vovels :',v)
    print(f'Conson :',c)
else:
    print('please enter only Alphabetes')'''

# WAP to print n natural number Sum. 

'''n=int(input("Enter any value : "))
sum=0
for i in range(1,n+1):
    sum=sum+i
    if(i<n):
        print(i,end='+')
    else:
        print(i,end='=')
print(sum)'''


# WAP to print n even number.

'''n=int(input("Enter any value : "))
sum=0
for i in range(1,n+1):
    sum=sum+2*i
    if(i<n):
        print((2*i-1),end='+')
    else:
        print((2*i-1),end='=')
print(sum)
'''
# WAP to print n even number.

'''n = int(input("Enter any value: "))
sum = 0

for i in range(1, n+1):
    odd = 2*i - 1
    sum = sum + odd

    if i < n:
        print(odd, end=",")
    else:
        print(odd, end="=")

print(sum)'''


                      # While loop  #
                      
# Syntex :-  initalization
#            while condition:
#                     {while-body executed when condition is True}   
# Exampal of while loop :- 

# count given number digit -->
'''n=eval(input("Enter any value : "))
td=0
while n>0:
    td=td+1
    n=n//10
print("Total digit = ",td)'''

# Check Armstrong number using while loop -->
'''n=eval(input("Enter any value : "))
n=eval(input("Enter any value : "))
m=p=n
td=sum=0
while n>0:
    td=td+1
    n=n//10
while m>0:
    ld=m%10
    sum=sum+ld**td
    m=m//10
if p==sum:
    print(f'Given number {p} is armstrong')
else:
    print(f'Given number {p} is not armstrong')'''

# check palindrom :-
'''s=input("Enter any name : ")
if s==s[ : :-1]:
    print(f'Givrn name {s} is Palindrom')
else:
    print("Not palindrom")    '''        

# WAP Revers String/number :- 
'''s=input("Enter any string : ")
s1=''
for i in s:
    s1=i+s1
print(f'Reversed string is :',s1) '''

# WAP to Check factor of given number :-
'''n=int(input("Enter any value : "))
i,l=2,[]
while i<n:
    if n%i==0:
        l.append(i)
    i=i+1
print(f'Factor of given number {n} is {l}')'''
 # 
    print(f'Given number {p} is not armstrong')

            
