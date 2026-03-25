# File-Handling :- 
#                     1. Create() / open()
#                     2. Write() / read()
#                     3. close()

# open() :- Syntex --> open('file_name.file_extention','modes')
#            modes :- x= create,
#                     w= write,
#                     r= read,
#                     a= append 

# Example :- WAP to create a file

#| Mode    | Creates New File | Works If File Exists         | Writable | Readable | Cursor Position  |
#| ------- | ---------------- | ---------------------------- | -------- | -------- | ---------------  |
#|   'x'   | ✔️ Yes           | ❌ No (error if file exists)| ✔️ Yes   | ❌ No   | Start (0th-index)|
#|   'w'   | ✔️ Yes           | ✔️ Yes (but overwrites!)    | ✔️ Yes   | ❌ No   | Start (0th-index)|
#|   'r'   | ❌ No            | ✔️ Yes (file must exist)    | ❌ No    | ✔️ Yes  | Start (0th-index)|
#|   'a'   | ✔️ Yes           | ✔️ Yes                      | ✔️ Yes   | ❌ No   | End (append)     |


# create a any extansion file like .py,.txt,.js,.html etc...
'''f=open('n1.txt','x')
f=open('n2.txt','x')
f=open('n3.txt','x')'''
# example
'''f=open('n6.txt','a+')
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.encoding)
print(f.closed)'''


# Write :- There is two type of write function.
#            1. write() :- Add a single string.
#            2. writelines() :- Add a multiple string.

# write() -->
'''f=open('n6.txt','a+')
data=' this is python class.\n'
f.write(data)
f.close()'''

# Writelines -->
'''f=open('n6.txt','a+')
data=['python\n','java\n','PHP\n']
f.writelines(data)
f.close()'''

# Read :- There is also have two function.
#           1. read() :- Read all data.
#           2. read(n) :- Read n-bit of data.
#           3. readline() :- Read single-line of data.
#           4. readlines() Read all-lines of data.

# read() -->
'''# f=open('n6.txt')  # By defualt supported read function
f=open('n6.txt','r+')
data=f.read()
# data=f.read(10)     # read(n) function
print('first :',data)
data=f.read(5)
print('last : ',data)
f.close()'''

# readline() -->
'''f=open('n6.txt','r+')
# data=f.readline()
data=f.readlines()   # data=f.readlines()
print(data)
f.close()'''


# Cursor-Movemant :- 
#                    1. tell() :- To check curser current position.
#                    2. seek() :- To move our curser to required position.

# tell() -->
'''# f=open('n7.txt','x+')
# f=open('n7.txt','w+')
f=open('n7.txt','r+')
# f=open('n7.txt','a+')
data=f.read(10)
print(data)
print(f.tell())'''

# seek() --> Syntex :- seek('How many bits are move','from where')  
#                               { 0 -->Starting-position,
#                                 1 -->Current-position,
#                                 2 -->Last-position }

'''f=open('n6.txt','rb+')
# print(f.tell())
# data=f.read(10)
# print(data)
# print(f.tell())
# f.seek(-5,1)
# print(f.tell())
# f.read(10)
# print(f.tell())
data=f.read(25)
f.seek(20)
print(f.tell())
f.seek(-1,2)
print(f.tell())
f.seek(-5,2)
data=f.read()
print(data)'''
