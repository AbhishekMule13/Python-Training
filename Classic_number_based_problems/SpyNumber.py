while True:
    num=int(input("Enter the number:"))
    add=0
    multi=1
    temp=num

    while temp>0:
        digit=temp%10
        add+=digit
        multi*=digit
        temp//=10

    if add == multi:
        print(f"{num} is a spy number!!!")
    else:
        print(f"{num} is not a spy number")

           
