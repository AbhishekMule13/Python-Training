def is_strong_number(nums):
    def factorial(n):
        fact=1
        for i in range (1,n+1):
            fact=fact*i
        return fact
    orignal=nums
    total=0
    while nums>0:
        digit=nums%10
        total+=factorial(digit)
        nums//=10 
    return total==orignal 
while True: 
    nums=int(input("Enter the number:")) 
    if is_strong_number(nums):
        print(f"{nums} is a strong number")
    else:
     print(f"{nums} is a not strong number")
