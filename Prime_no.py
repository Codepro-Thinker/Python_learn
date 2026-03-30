# Program to check whether a number is prime or not

n = int(input("Enter a number: "))
if n <= 1:
    print("The number is NOT a prime number.")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("The number is NOT a prime number.")
            break
    else:
        print("The number is a Prime number.")