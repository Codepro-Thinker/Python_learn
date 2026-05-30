# Program to check whether a number is Armstrong or not

n = int(input("Enter a number: "))
sum = 0
temp = n
num_digits = len(str(n))

while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

if n == sum:
    print("The number is an Armstrong number.")
else:
    print("The number is NOT an Armstrong number.")