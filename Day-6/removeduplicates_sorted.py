#Removing duplicates with Set

# Method - 1 (Sets)

def remove_duplicates(arr):
    update = set(arr)
    count = len(update)
    return update, count


arr = [1,2,1,7]
result = remove_duplicates(arr)
print(result)


# -------------------------

# Method - 2 (Dictionary)

def remove_duplicates(arr):
    n = len(arr)
    numbers = {}

    for i in range(0,n):
        numbers[arr[i]] = 0

    j = 0
    for key in numbers:
        arr[j] = key
        j += 1

    return j

arr = [1,2,1,7]
result = remove_duplicates(arr)
print(result)


# --------------------------

# Method - 3 (Two Pointers)

def remove_duplicates(arr):
    n = len(arr)
    i = 0
    j = i+1     #We will iterate j and swap if any number is unique, with i+1

    while j<n:    #The j loop goes from 1 to last
        if arr[j] != arr[i]:
            i += 1      #Increment i for next element and then swap
            arr[i], arr[j] = arr[j], arr[i]    
        j+=1

    return i+1   
        

arr = [1,1,1,3,3,3,3,5,6,7,7]
result = remove_duplicates(arr)
print(result)
