# WAP to create a calculater 
while (True):
    print("1. Add\n 2. Sub\n 3. Div\n 4. Multi\n 5.Exit")
    n=int(input("Please Enter above value : "))
    if n in (1,2,3,4,5):
        if n in (1,2,3,4):
            if n==1:
                numbers=int(input("How many numbers you want to add : "))
                l=[]
                for i in range(1,numbers+1):
                    value=int(input(f'Enter {l} number '))
                    l.append(value)
                sum=0
                for i in l:
                    sum+=i
                print(f'Addition of {l} is {sum}')
        else:
            break
    else:
        print("Please Enter valid Choices : ")