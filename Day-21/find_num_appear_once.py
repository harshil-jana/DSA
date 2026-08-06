# Find Number Which Appears Once 

# Method - 1 (Linear Search)

class Solution:
    def findNumappearOne(self, arr: list[int]) -> int:
        n = len(arr)

        for i in range(0,n):
            num = arr[i]
            count = 0

            for j in range(0,n):     # Check how many times number appeared
                if arr[j] == num:
                    count += 1

            if count == 1:  # If it appears once, return the number
                return num

        return -1
    
sol = Solution()
arr = [2,2,1]
print(sol.findNumappearOne(arr))          
