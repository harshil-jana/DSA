Factorial of a number (Iterative)


def factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact *= i
    
    return fact

print(factorial(0))


# ---------------------------------

# Factorial (Recursion)

# def factorial_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial_recursive(n-1)

# a = factorial_recursive(5)
# print(a)
