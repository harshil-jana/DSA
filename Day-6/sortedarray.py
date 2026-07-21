def sortedarray(arr):
    count = 0
    n = len(arr)
    for i in range(0,n-1):
        if arr[i] < arr[i+1]:
            count += 1
    if count == n-1:
        print("True")
    else:
        print("False")
            

arr = [1,2,1,7]
result = sortedarray(arr)

        