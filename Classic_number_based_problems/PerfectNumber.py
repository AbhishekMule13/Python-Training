while True:
    num=int(input("Enter the number:"))

    if num<1:
        print("Please Enter the positive number")
        continue
    
    total=0
    for i in range(1, num):
        if num%i==0:
            total+=i
            
    if total==num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")        
