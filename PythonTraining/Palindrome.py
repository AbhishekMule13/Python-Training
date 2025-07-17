def palindrome(s):
    return s==s[::-1]
word=input("Enter the word:")
print(palindrome(word))