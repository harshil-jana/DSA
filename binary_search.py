def binary_search(arr, target):
    n = len(arr)
    start = 0
    end = n-1
    
    
    while (start<=end):
        mid = (start + end)//2
        if arr[mid] == target:
            return (f"The target is found at index {mid}")
        elif arr[mid] < target:
            start = mid+1
        elif arr[mid] > target:
            end = mid-1

    return -1

numbers = [-1,0,3,5,9,12]
target = 13
binary = binary_search(numbers, target)
print(binary)