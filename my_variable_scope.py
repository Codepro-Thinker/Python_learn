# Variable Scope :-  There are three of variable.
#                       1. Local variable.
#                       2. Globle variable.
#                       3. Non-Local variable.

# Local :-  Access with in block.

'''def display():
    x=10         # Local variable
    print(x)
display()
print(x) '''       # NameError: name 'x' is not defined

# To convert local variable to globle variable.
'''def display():
    global x     # Useung globle key-word to create a local variable to globle variable.
    x=10         # Local variable
    print(x)
display()
print(x) '''

'''def display():
    global x
    x=10         # Local variable
    print(x)
# print(x)
display()
print(x) '''

# Globle :- 

'''x=20             # globle variable
def show():
    print(x)
print(x)       
show()
print(x)'''


'''x=20             # globle variable
def show():
    x=30
    print(x)
print(x)        # o/p --> 20
show()          # o/p --> 30
print(x)    '''    # o/p --> 20

'''x=20             # globle variable
def show():
    print(x)  # because local x kii priority jada hai to givrn a error.
    x=10
    print(x)
print(x)       
show()
print(x)'''

'''x=20             # globle variable
def show():
    x=10
    print(globals()['x'])     # to print a globle variable value until localvariable.
show()'''

# Non-Local :- 
def show():
    x=10
    def display():
        nonlocal x    # allow to give a x value in a local variable.
        x=x+5
        print(x)
    display()
show()

