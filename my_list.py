# List() :- 1. collection of element.
#           2. indexing supported.
#           3. slicing suppoted.
#           4. dublicates are allowed.
#           5. mmutable in nature.
#           6. Represented by [] and comma (,) seperated.

'''l=[10,20,'python',10,'java']
print(l)
print(type(l))'''

'''l=[10,20,'python','java',30]
l1=['python','java','php']
print(max(l))
print(min(l))
print(sum(l))
print(len(l))
print(id(l))
print(type(l))
print(max(l1))
print(min(l1))
# print(sum(l1))  not supported.
print(len(l1))
print(id(l1))
print(type(l1))'''


# List Method :- There are have  11 method in list.

# append() --> Add single element in last position.
# copy()) --> Create new object with same elements.
# clear() --> Clear all elements from list.
# index() --> Findout order/location of any elements.
# count() --> Findout freq of any element.
#   pop() --> Remove index targeted element by-default it remove -1 index elements.
# remove() --> Remove targeted element.
# extend() --> Add multiple elements at last position.
# insert() --> Add element in targeted position.
#   sort() --> To arrenge all elenemts in assending order.
#  reverse() --> To reverse all given elements.


#l=[2,4,6,8,'python',3,2,5]

#n=eval(input("Enter any value"))

# print(l.append(n))
# print(l.extend(n)) # variable collection hona chahiyee.
#print(l.insert(5,n)) # insert(5,n) 5 is a position of index.
'''l.clear()
print(l)
print(id(l))
del l   # It's use too delete memory address in disk/computer.
print(l)

l1=l.copy()
print(l,l1)
print(id(l),id(l1))

print(l.pop())
l.pop(0)
print(l)

l.remove('python')
print(l) 

print(l.index('python'))

print(l.count('python'))


l1=[10,50,30,90,40,20]
l1.sort()  # Assending order.
l1.reverse()
l1.sort(reverse=True)  # Dissending order.
print(l1)'''


# Tuple's :- 1. Collection of elements.
#            2. Represented by () with comma(,) seperated elements.
#            3. Ordered collection.
#            4. Indexing supported.
#            5. slicing suppoted.
#            6. dublicates are allowed.
#            7. immutable in nature.

'''t=(1,2,3,4,5,6)

print(t)
print(type(t))
print(len(t))
print(id(t))
print(max(t))
print(min(t))
print(sum(t))'''

# Tuple's Method :- 

'''t=(1,2,5,'python')

print(t.index(2))
print(t.count(4))'''


# Dictionary :- 1. Collection of 'key value pair',Where 'key' and 'value' is seperated by (:)
#               2. Represented by { } with comma(,) seperated pairs.  --> {'key':'value','key2':'value2"}
#               3. Key must be unique but value may be dunlicate.
#               4. Mapped data-type.
#               5. Indexing not supported.
#               6. Slicing not supported.
#               7. Mutable in nature.

'''d={'name':'Shubham','age':'19','place':'Bhopal','quality':'B.tech'}
d1={1:'name',2:'age',3:'home'}
print(d)
print(type(d))
print(len(d))
print(id(d))
print(max(d))
print(min(d))
print(sum(d1))   # UNsupporeted'''

# Dictionary Method :- 

'''d={'name':'Shubham','age':'19','place':'Bhopal','quality':'B.tech'}
d1={1:'name',2:'age',3:'home'}

d2=d.copy()
print(d,d2)
print(id(d),id(d2))
d.clear()
print(d)
del d
print(d)
print(d.get('age'))
print(d.values())
print(d.keys())
print(d.items())      # important.
d.update(d1)
print(d)
print(d.pop('age'))  # delete using key word.
print(d)
d.popitem()       #  delete last pair of key-value.
print(d)
print(d.fromkeys(d1,58))
s=['name','email','contact','add']
d.fromkeys(s)
n=input("Enter your name :")
e=input("Enter your Email :")
c=input("Enter your contact number :")
a=input("Enter your Address :")
d['name']=n
d['email']=e
d['contact']=c
d['add']=a
print(d)

print(d.setdefault('bro','naveen'))
print(d)'''


# Set() ;- 1. Collection of unique elements.
#          2. Represented by {} with comma(,) seperated elements.
#          3. Unorded collection.
#          4. Indexing not suppoted.
#          5. Slicing not supported.
#          6.  Mutable in nature.

'''s={10,20,'python','java','php'}
s1={10,20,30,40,80,70}
print(s)
print(s1)
print(type(s))
print(len(s))
print(id(s))
print(max(s1))
print(min(s1))
print(sum(s1))'''

# Set Method :- There are 2 types of method 
#              1. That required more tham one set.
#              2. That required only one set.

'''s1,s2={1,2,3,4,5},{4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

Updates methods :- 

s1.intersection_update(s2)   # updated given set exiting set.
print(s1)
print(s2)

s1.difference_update(s2)
print(s1)
print(s2)
print(s1.intersection_update(s2))'''

'''s1,s2={1,2,3,4,5,6,7,8,9},{5,6,7,8,9}
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))
s1,s2={1,2,3,4,5},{6,7,8,9,10}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))    # a single comman elements is not call disjoint but not a single elements is same in given set is called disjoints.

s={1,2,3,4,5,6,8}
s2={2,4,6,8,10,12}
s1=s.copy()
print(s1)
print(id(s1),id(s))
s.clear()
print(s)
del s
print(s)
s.add('python') #  add single element.
print(s)
s.update(s2) #  add multiple elements.
print(s)
print(s.pop())  # random element remove.
s.remove(5) 
print(s)    # remove targeted elements.
s.discard('python')
print(s)'''


# Frozonset :- 1. Coleection of unique elements.
#              2. Represented by {} with comma(,) seperated elements.
#              3. Unorded collection.
#              4. Indexing not suppoted.
#              5. Slicing not supported.
#              6. IMMutable in nature.

'''s='python'
l=[10,20,30,'python']
t=(1,2,3,4,'java')

fs1=frozenset(s)
print(fs1,type(fs1))
fs2=frozenset(l)
print(fs2,type(fs2))
fs3=frozenset(t)
print(fs3,type(fs3))

print(len(fs2))
print(type(fs2))
print(id(fs2))

fs1=frozenset({1,2,3,4,5})
fs2=frozenset({4,5,6,7,8})
print(fs1.union(fs2))
print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.symmetric_difference(fs2))
print(fs1.isdisjoint(fs2))
print(fs1.issuperset(fs2))
print(fs1.issubset(fs2))
print(fs1.copy())'''

