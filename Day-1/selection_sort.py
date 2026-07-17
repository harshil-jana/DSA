def selection_sort(arr):
    n = len(arr)
    
    

    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
             
    return arr 
    

unsorted = [12,25,11,34,90,22]
sorted = selection_sort(unsorted)
print(f"Sorted list = {sorted}")