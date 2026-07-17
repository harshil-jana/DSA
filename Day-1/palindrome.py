def palindrome(num):
    reverse = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        reverse = (reverse * 10) + digit
        temp //= 10

    if reverse == num:
        print("palindrome")
    else:
        print("not a palindrome.")

palindrome(14541)