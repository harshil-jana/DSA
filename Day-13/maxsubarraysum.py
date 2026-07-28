# Maximum SubArray Sum

# Method - 1 (Brute Force)

def maxsubarraysum(nums):
    n = len(nums)
    max_s = float("-inf")
    if n == 1:
        return nums[0]
    for i in range(0,n):
        total = 0
        for j in range(i,n):
            total += nums[j]
            max_s = max(max_s, total)

    return max_s

nums = [-2,-1]
print(maxsubarraysum(nums))


# --------------------------------

# Method - 2 (Optimal Solution - Kadane's Algorithm)

def maxsubarraysum(nums):
    n = len(nums)
    max_s = float("-inf")
    total = 0

    for i in range(0,n):
        total += nums[i]
        max_s = max(max_s, total)
        if total < 0:
            total = 0
    return max_s

nums = [-2,-1]
print(maxsubarraysum(nums))