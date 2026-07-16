def fibonacci():
    n = int(input("Enter the numbers of terms : "))
    a = 0
    b = 1

    for i in range(n):
        
        next_num = a + b
        a = b
        b = next_num
    return b

print(fibonacci())