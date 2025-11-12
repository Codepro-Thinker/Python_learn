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