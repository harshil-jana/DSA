# #Fibonacci Series

# def fibonacci(n):

#     a = 0
#     b = 1

#     for i in range(n):
#         print(a, end=" ")
#         next_num = a + b
#         a = b
#         b = next_num

# fibonacci(5)

# -------------------------

#Fibonacci Sequence (Using recursion)

def fibonacci_sequence(num):  #F(n) = F(n-1) + F(n-2)
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci_sequence(num-1) + fibonacci_sequence(num-2)

result = fibonacci_sequence(4)
print(result)