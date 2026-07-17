# import array

# arr = array.array("i", [1,2,3,4])
# print(arr)
# arr[1] = 90
# print(arr)

#LINEAR SEARCH

# import array
# def linear(arr):
    
#     target = (input())
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#         break

# arr = array.array("i", [1,4,6,4,6])
# linear(arr)



#LIST

target = int(input("Enter the target : "))  

def linear(numbers):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return (f"The target is present at the index {i}")
    return -1


numbers = list(map(int, input("Enter the numbers : ").split()))
print(linear(numbers))