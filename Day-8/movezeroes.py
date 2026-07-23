# Move Zeroes

# Method - 1 (Brute Force)

def movezeroes(nums):
    n = len(nums)
    temp = []
    for i in range(0,n):
        if nums[i] != 0:
            temp.append(nums[i])
    n2 = len(temp)
    for i in range(0,n2):
        nums[i] = temp[i]
    for i in range(n2,n):
        nums[i] = 0
    return nums

nums = [1,0,2,4,3,0,0,3,5,1]
result = movezeroes(nums)
print(result)

# ------------------------------
# Method - 2 (Own Method)

def movezeroes(nums):
    n = len(nums)
    i = 0
    k = nums.count(0)
    p = 0
    while i < n:
        if nums[i] == 0:
            p += 1
            nums.pop(i)
            nums.append(0)
            i -= 1
            if p == k:
                break
        i += 1
    return nums

nums = [1,0,2,4,3,0,0,3,5,1]
result = movezeroes(nums)
print(result)


# ------------------------------

# Method - 3 (Optimal Solution)

def movezeroes(nums):
    n = len(nums)
    if n == 1:
        return
    i = 0
    while i < n:
        if nums[i] == 0:
            break
        i+=1
    if i == n:         #If i == n, that means there is no zero in the array.
        return
    j = i+1
    while j < n:
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
        j+=1

    return nums
        
nums = [1,0,2,4,3,0,0,3,5,1]
result = movezeroes(nums)
print(result)


