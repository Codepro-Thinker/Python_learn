# Triangle pattern :- 

# 1.Right side Triangle -->
'''n=int(input("Enter Row number : "))
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i) '''
        

# Print Triangle -->
'''n=int(input("Enter Row number : "))
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i) '''


# Rght side Triangle -->
'''n=int(input("Enter Row number : "))
for i in range(1,n+i):
     print(' '*i+'*'*(n-i))  '''

# Print lower Triangle --.
'''n=int(input("Enter Row number : "))
for i in range(n):
     print(' '*i+'* '*(n-i)) '''


# Right side lower Triangle -->
'''n=int(input("Enter Row number : "))
for i in range(n):
     print(' '*i+'*'*(n-i)) '''

# Left side lower Triangle -->
'''n=int(input("Enter Row number : "))
for i in range(n):
     print('* '*(n-i)) '''


# marge right upper and lower Tiangle -->
'''n=int(input("Enter Row number : "))
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)
for i in range(n-1,0,-1):
        print(' '*(n-i)+'*'*i)'''

#  Print Daimand shap -->
'''n=int(input("Enter Row number : "))
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i)
for i in range(n-1,0,-1):
        print(' '*(n-i)+'* '*i)'''

# Marge Left upper and lower Tiangle -->
n=int(input("Enter Row number : "))
for i in range(1,n+1):
    print('* '*i)
for i in range(n-1,0,-1):
        print('* '*i)   