# Conditional Statements :- 
#                           1. if statement (single condition)
#                           2. if-else statement
#                           3. if-elif statement (Multiple condition)
#                           4. if-elif-else statement


# if statement :-  block may be executed.
# Syntex -->  if(condition): {if-body executed when given condition is True}

'''n=int(input("enter the value"))
if(n>=1):
    print("Given number is positive")'''

# if-else statement :-     
# Syntex -->  if(condition): {if-body executed when given condition is True}
#             else:  {else block executed when given condition is False}

'''n=int(input("enter the value"))
if(n>=1):
    print(f'Given number {n} is positive')
else:
    print(f'Given number {n} is either zero or negative')  '''  

# if-elif statement :- block may be executed.
#                Syntex -->       if(condition): 
#                                           { if-block}
#                                 elif(condition):
#                                           { elif-block }

'''n=int(input("enter the value"))
if(n>=1):
    print(f'Given number {n} is positive')
elif(n==0):
    print(f'Given number {n} is zero ')  '''

# if-elif-else statement :- 
#                Syntex -->       if(condition): 
#                                           { if-block}
#                                 elif(condition):
#                                           { elif-block }
#                                 else:
#                                     {else-block}

'''n=int(input("enter the value"))
if(n>=1):
    print(f'Given number {n} is positive')
elif(n==0):
    print(f'Given number {n} is either zero')  
else:
    print(f'Given n umber {n} is negative')'''



# Question 1 ;-

'''age=float(input("enter person Age"))
if(0<age<18):
    print(f'According to Age  {age} person is Child')
elif(17<age<60):
    print(f'According to Age {age} person is Adult')  
elif(59<age<100):
    print(f'According to Age {age} person is Old')
else:
    print(f'Given Age {age} is Invalid')
'''

# Question 2 :-

h=float(input("Enter Hindi marks"))
if(0<=h<=100):
    e=float(input("Enter English marks"))
    if(0<=e<=100):
        m=float(input("Enter Math marks"))
        if(0<=m<=100):
            s=float(input("Enter Science marks"))
            if(0<=s<=100):
                s_s=float(input("Enter Social Science marks"))
                if(0<=s_s<=100):
                    avg=((h+e+m+s+s_s)/5)
                    if(0<=avg<=34):
                        print(f'fail {avg}')
                    elif(35<=avg<=44):
                        print(f'3rd Division {avg}') 
                    elif(45<=avg<=59):
                        print(f'2nd Division {avg}')
                    else:
                        print(f'1st Division {avg}')
                else:
                    print(f'Invalid number')
            else:
                print(f'Invalid number')
        else:
            print(f'Invalid number')
    else:
        print(f'Invalid number')
else:
    print(f'Invalid number')
                   
                
