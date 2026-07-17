# With while loop

def armstrong(num):
    count = 0
    total = 0
    temp = num

    while temp > 0:   #while loop for counting the number of digits
        temp //= 10
        count += 1

    temp = num

    while temp > 0:   #while for calculating the total
        digit = temp % 10
        total += (digit ** count)
        temp //= 10

    if total == num:
        print(f"{num} is an armstrong number.")
    else:
        print(f"{num} is not an armstrong number.")


result = armstrong(153)

# -----------------------------------

# With str count

def armstrong(num):
    count = len(str(num))
    total = 0
    temp = num

    while temp > 0:   #while for calculating the total
        digit = temp % 10
        total += (digit ** count)
        temp //= 10

    if total == num:
        print(f"{num} is an armstrong number.")
    else:
        print(f"{num} is not an armstrong number.")


result = armstrong(153)