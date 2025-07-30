while True:
    num=int(input("Enter the number:"))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit
        temp//=10

    if num%sum==0:
        print(f"{num} is Harshad number!!!")
    elif sum==0:
        print("Sum is divisiable")
    else:
        print(f"{num} is not Harshad number")


