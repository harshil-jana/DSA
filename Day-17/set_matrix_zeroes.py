# Set Matrix Zeroes

# Method - 1 (Brute Force)

class Solution:
    def infinity(self, matrix, row, col) -> None:
        r = len(matrix)
        c = len(matrix[0])

        for i in range(0,r):
            if matrix[i][col] != 0:       # We have to check the elements which are not zeroes and make them infinity
                matrix[i][col] = float("inf")

        for j in range(0,c):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")

    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == 0:
                    self.infinity(matrix,i,j)

        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0
        print(matrix)

sol = Solution()
matrix = [[7,10,29,3],[1,20,0,4],[19,0,6,11],[4,27,14,7]]
result = sol.setZeroes(matrix)


# ----------------------------------

# Method - 2 (Optimal Solution)

class Solution:
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        row_track = [0 for _ in range(r)]     # If we get a zero, corresponding element row = -1
        col_track = [0 for _ in range(c)]    # If we get a zero, corresponding element column = -1

        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == 0:      
                    row_track[i] = -1       # We are keeping them as -1's.
                    col_track[j] = -1

        for i in range(0,r):
            for j in range(0,c):
                if row_track[i] == -1 or col_track[j] == -1:   # If the any one of the corresponding element in track has -1, element = 0
                    matrix[i][j] = 0

        print(matrix)

sol = Solution()
matrix = [[7,10,29,3],[1,20,0,4],[19,0,6,11],[4,27,14,7]]
result = sol.setZeroes(matrix)