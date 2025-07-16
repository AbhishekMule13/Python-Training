
def factorial(x):
    if(x==0 or x==1):
        return 1
    else:
        return x * factorial(x-1)
while True:
    try:
        num=int(input("Enter a num to generate a factorial:"))
        if(num==-1):
            print("Existing the code")
            break

        if (num < 0):
            print("Factorial will be not defined")
        else:
            result = factorial(num)
            print(f"Factorial of {num} is {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")


