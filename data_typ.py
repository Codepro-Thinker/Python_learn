# Data types:- 
# Intger :-

'''x=10
print(x)
print(type(x))
print(id(x))'''

# String :- 1. collection of characters.
#           2. indexing supported.
#           3. slicing suppoted.
#           4. dublicates are allowed.
#           5. immutable in nature.


# Python inbulid function :- print(),type(),id(),len(),max(),min(),sum(),input()

# sasscii key value --> ''=32, 0-9=47-58, A-Z=65-90,a-z=97-122
'''s='python'
print(s)
print(type(s))
print(id(s))
print(len(s))
print(max(s))
print(min(s))
print(sum(s))   # unsuppoeted for string.'''


# Methods :- lower(),upper(),index(),split(),join(),find(),replace() etc.
'''s='python'
s1='NAVEEN'
print(s.swapcase())
print(s1.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.index('y'))
print(s.find('Y'))
print(s1.count('N'))'''

# join() Syntex :- 'seprater'.join(iterater/collection) 

'''s1='python'
s2='java'
s3='php'
#l=[s1,s2,s3]
s=' '.join([s1,s2,s3])
print(s)'''

# Split() Syntex :- string.slipt('seperater')
#                   string.slipt(seperater','how many time')

'''s='This is python class'
#l=s.split('s')
#l=s.split()
l=s.split('s',2)
print(l)'''

# Replace() Syntex:- 

# s='This is python'
# print(s.replace('This','z',1))



# List() :- 1. collection of element.
#           2. indexing supported.
#           3. slicing suppoted.
#           4. dublicates are allowed.
#           5. mmutable in nature.
#           6. Represented by [] and comma (,) seperated.

'''l=[10,20,'python',10,'java']
print(l)
print(type(l))'''


# Operator in String :-

#s1,s2='python','java'
# print(s1+s2)   #  sign + is called concatication.
# print(s1-s2)   # error unsupported for string
#print(s1*2)
#print('a'>'A')   # All compation operator are work in srting.
'''print('Python' > 'Pava')
print('Nveen' < 'Piyush')
print('himmanshu' == 'Pooja')
print('Kammo' > 'Tillu')'''

'''x='python'
y='java'
print(y and x)
z=''
print(x and z)
x='a'
print(bool(x))'''

# Logical :- And 

'''s1=''
s2=''
print(s1 and s2)

s1,s2='','python'
print(s1 and s2)

s1,s2='python',''
print(s1 and s2)

s1,s2='python','java'
print(s1 and s2)
'''

# s1,s2='PYTHON','java'
# print(s1 and s2)


# Logical :- OR

'''s1=''
s2=''
print(s1 or s2)

s1,s2='','python'
print(s1 or s2)

s1,s2='python',''
print(s1 or s2)

s1,s2='python','java'
print(s1 or s2)
'''

# s1,s2='PYTHON','java'
# print(s1 or s2)

# LOgical :- NOT --> not supported string.

# MEMBERSHIP :- in.not in

'''s='aeiouAEIOU'
s1='p'
print(s1 in s)
s2='ae'
print(s2 in s)
s3='ea'
print(s3 in s)'''

# Identity :- is,is not

'''s1='python'
s2='java'
print(s1 is s2)'''

# Bitwise operayor :- It's is not applicable for string.



