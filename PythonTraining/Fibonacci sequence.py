#from operator import truediv


''''
def fibonacci_sequence(x):
    a=0
    b=1
    for s in range(x):
       # yield a
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
        print("Invalid input..")'''






def fibonisis(x):
    a=0
    b=1
    for i in range (x):
        yield a
        a,b=b,a+b
while True:
    try:
        num=int(input(print("Enter the no of febonisis terms (Enter -1 for exit:)")))
        if  num==-1:
            print("exit")
            break
        elif num>0:
            print(f"fibonaccies series is: {list(fibonisis(num))}")
        else:
            print("Please enter positive no!!!")    
    except ValueError:
           print("Invalid input")




