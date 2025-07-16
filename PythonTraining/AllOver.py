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









