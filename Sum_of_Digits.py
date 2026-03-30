# Program to calculate sum of all digits in a given integer

n = int(input("Enter an integer: "))
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print("Sum of all digits is:", sum)