
#A 'n' number of list when in 1st no go to the stack then 2nd no add in 1st no then 3rd no substract to the addition of 1st and 2nd 
#Example:::[12 13 14 18 17 12 11]=13
while True:
    num=list(map(int, input("Enter the list of num:(Sprated by spaces):").split()))
    result=num[0]
    for i in range(0,len(num)):
        if i % 2!=0:
            result+=i
        else:
            result-=i

    print("Result is:", result)        

        












