from operator import truediv


def fibonacci_sequence(x):
    a=0
    b=1
    for s in range(x):
        yield a
        a , b = b ,a + b
while True:
    try:
        num = int(input("Enter the number of Fibonacci terms (Enter -1 for exit):"))
        if num==-1:
            print("THANK YOU!!!")
            break
        if num > 0:
            print(f"Fibonacci sequence is: {list(fibonacci_sequence(num))}")
        else:
            print("Please enter positive number!!!")

    except ValueError:
        print("Invalid input..")





