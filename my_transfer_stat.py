# Transfer Statement :- 
#                       1. Continue :- To skip current iteration.
#                       2. Break :- To terminate current loop.
#                       3. pass :- To skip current block.


# Example of continue :-
# while loop:-
'''n=int(input('Enter any value : '))
i=1
while i<=n:
    if i==5:
#        print('helo')
        continue
    else:
        print(i)
    i=i+1'''
# Or
'''n=int(input('Enter any value : '))
i=1
while i<=n:
    if i==5:    #skip number 5
        i=i+1
        continue
    else:
        print(i)
    i=i+1'''

# for loop :- 
'''n=int(input('Enter any value : '))
for i in range(1,n+1):
    if i==5:        # skip number 5 
        continue
    else:
        print(i)'''
    

# Example of pass :- 
'''n=int(input('Enter any value : '))
i=1
while i<=n:
    if i==5:
#        print('helo')
        pass
    else:
        print(i)
    i=i+1'''

# Example of break :- 
'''n=int(input('Enter any value : '))
i=1
while i<=n:
    if i==5:
        break
    else:
        print(i)
    i=i+1'''