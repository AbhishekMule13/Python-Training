def is_strong_number(num):
    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    return factorial(num)
n=4       
result = is_strong_number(n)
print("Factorial of", n, "is", result)   