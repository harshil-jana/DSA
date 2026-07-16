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

    return "The target is not present in the array."

numbers = [13,24,27,35,50]
target = 70
binary = binary_search(numbers, target)
print(binary)