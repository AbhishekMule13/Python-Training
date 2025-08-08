#Even or odd
'''num=int(input(print("Number which is Even or Odd:")))
if(num%2==0):
    print("{num} is even number")
else:
    print("{num} is odd number")
'''


#concatenate two strings

'''str1="abhi"
str2="mule"
print(str1+"  "+str2)
'''

#count the number of vowels in a string

'''def count_vowels(s):
    vowels = "aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count
line=(input("Enter a string:"))
print(f"The vowels in string is {count_vowels(line)}")
'''

#Area of rectangle

'''def Area_rectangle(length,breadth):
    return length*breadth
length=int(input("length of the rectangle:"))
breadth=int(input("Breadth of the rectangle:"))
print(f'Area of rectangle:{Area_rectangle(length,breadth)}')
'''

#find common elements in two lists
'''list1=list(map(int,input("Enter list1:").split()))
list2=list(map(int,input("Enter list2:").split()))
common_element=list(set(list1) & set(list2))
print("Common elements:",common_element)
'''

#string is a palindrome
'''def palindrome(s):
    return s==s[::-1]
word=input("Enter the word:")
print(palindrome(word))
'''


#print("Hello World")


'''
nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            exit()
            '''



#Add two lists
'''
list1=['1','2','4']
list2=['1','2','3']
s=list1+list2
s.sort()
print(s)
'''

#Int to binary
'''
s=27
print(bin(s))
'''


'''
class Solution(object):
    def isPalindrome(self, s):
        cleaned = ''
        for char in s:
            if char.isalnum():
                cleaned += char.lower()  
        return cleaned == cleaned[::-1]
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))  #  True
print(s.isPalindrome("race a car"))                      #  False
print(s.isPalindrome(" "))                               #  True
'''

'''
s = "A man, a plan, a canal: Panama"
s=s.lower()
print(s)
'''
'''
num=[1,2,3,4,5,6,7,8,9,10]
for char in num:
    if (char%2==0):
        print(char," Square=",(char**2))
    else:
        print(char," Cube=",(char**3))

result=[char**2 if char%2==0 else char**3 for char in num]
print(result) 

result=[char for char in num  if char%2==0]
print(result)
'''


#Merge Sort list
'''
list1=[1,3,4,8,0,0,0,0]
list2=[5,4,6,0,1]
a=list1[:4]
b=list2[:5]
c=a+b
c.sort()
c.remove(0)
print(c)
'''


#Spy Number
'''
while True:
    num = int(input("Enter a number: "))

    sum_digits = 0
    product_digits = 1
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_digits += digit
        product_digits *= digit
        temp //= 10

    if sum_digits == product_digits:
        print(f"{num} is a Spy number\n")
    else:
        print(f"{num} is NOT a Spy number\n")
'''

#Harshad number
'''
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
'''

#Duck number
'''
def is_duck_no(num_str):
    if num_str[0]=='0':
        return False
    return '0' in num_str[1:]
num=input("Enter the number:")
if num.isdigit():
    if is_duck_no(num):
        print("It is a Duck Number.")
    else:
        print("It is NOT a Duck Number.")
else:
    print("Invalid input! Please enter only positive digits.")
'''































