def max_consecutive(arr):
    count = 0
    max_count = 0

    for i in range(0,len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max(max_count, count)

nums = [1,0,1,1,0,1]
print(max_consecutive(nums))