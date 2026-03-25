# Q.1(a) Write a Python program to change a given string to a newly 
# string where the first and last chars have been exchanged.
# Example: Input:”welcome” Output:”eelcomw”
# Solution :-
'''s = input("Enter any  string: ")
if len(s) > 1:
    char = list(s)
    char[0], char[-1] = char[-1], char[0]
    new_s = ''.join(char)
else:
    new_s = s
print("New string is :", new_s)'''



# Q.1(b) Write a Python program to count the occurrences of each word in a
# given sentence.
# Example:
# Input:”welcome to cybrom”
# Output:3
# Solution :-
'''sentence = input("Enter a sentence: ")
words = sentence.split()
print("Total number of words:", len(words))'''


# Program to count occurrences of each word in a sentence

'''sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
for i in words:
    word_count[i] = word_count.get(i, 0) + 1
print("Word occurrences:")
for i, count in word_count.items():
    print(i, ":", count)'''

#       OR

'''from collections import Counter;
print(Counter(input("Enter any sentence: ").split()))
'''

# Logical Operater


# x=10
# y=20
# z=15
# print(x>y) and (x<z)
#print(x<y) or (x>z)
#print(not((x>y) or (x<z)))
#print(not(x>y))

x='python'
y='java'
z='kala'
a=' '
print(x not y)
print(y or x)
print(x and y and z)
print(a or x)