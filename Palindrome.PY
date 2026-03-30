# Program to check whether a string is palindrome or not

s = input("Enter a string: ")
if s == s[::-1]:
    print("The string is a Palindrome.")
else:
    print("The string is NOT a Palindrome.")