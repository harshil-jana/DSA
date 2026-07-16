def bubble_sort(arr):
    n = len(arr)
    for passes in range(0,n):
        for j in range(0,n-1-passes):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

unsorted = [12,25,11,34,90,22]
sorted = bubble_sort(unsorted)
print(f"Sorted list = {sorted}")