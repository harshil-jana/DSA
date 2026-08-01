# # 2D Matrix - Representation in Python

nums = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(nums)        # Rows = The number of sublists present in the main list
cols = len(nums[0])     # Columns = Any length of the sublist (as lengths of all the columns are equal in a matrix)

# # Iterating 2D matrix

for i in range(0,rows):
    for j in range(0,cols):
        print(nums[i][j], end = " ")       # Unpack the list and add " " in between the numbers
    print()      # Goes to new line after every i iteration

# ---------------------------------

# Print Upper Triangle

# 1 2 3   
# * 5 6   
# * * 9 

nums = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(nums)
cols = len(nums[0])

for i in range(0,rows):
    for j in range(0,cols):
        if j>=i:
            print(nums[i][j], end = " ")
        else:
            print("*", end=" ")
    print()


#----------------------------------------

# Print Lower Triangle

# * * * 
# 4 * *  
# 7 8 * 

nums = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(nums)
cols = len(nums[0])

for i in range(0,rows):
    for j in range(0,cols):
        if i>j:
            print(nums[i][j], end = " ")
        else:
            print("*", end = " ")
    print()


#----------------------------------------

# Print Diagonal of the Matrix

# 1 * *
# * 5 *
# * * 9

nums = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(nums)
cols = len(nums[0])

for i in range(0,rows):
    for j in range(0,cols):
        if i==j:
            print(nums[i][j], end = " ")
        else:
            print("*", end = " ")
    print()


#----------------------------------------

# Print Transpose of a Matrix

# 1 2 3    ==   1 4 7
# 4 5 6    ==   2 5 8
# 7 8 9    ==   3 6 9

# Method - 1 (Same Order 3 * 3)

nums = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(nums)
cols = len(nums[0])

for i in range(0,rows):
    for j in range(0,cols):
        if i<j:
            nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
        print(nums[i][j], end = " ")
    print()

# Method - 2 (Different Order)

nums = [[1,2],[3,4],[5,6]]    # Rows = 2, Columns = 3
rows = len(nums)
cols = len(nums[0])
result = [[0]*rows for _ in range(cols)]

for i in range(0,rows):   # Create a new list of transpose matrix with zeroes and replace with main elements
    for j in range(0,cols):
        result[j][i] = nums[i][j]
print(result)

