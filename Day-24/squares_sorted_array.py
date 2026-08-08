# Squares of a Sorted Array

# Method - 1 (Squares & Sort) - TC : O(N log N) and SC : O(1)

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(0,n):
            nums[i] **= 2
        nums.sort()
        return nums

sol = Solution()
arr = [-4,-1,0,3,10]
print(sol.sortedSquares(arr))  


# ---------------------------------------

# Method - 2 (Two Pointers) - TC : O(N) and SC : O(N)

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        i = n-1
        l = 0
        r = n-1

        while l<=r:
            if abs(nums[l]) <= abs(nums[r]):
                result[i] = nums[r]**2
                r -= 1
            else: 
                result[i] = nums[l]**2
                l += 1

            i -= 1
        return result

sol = Solution()
arr = [-4,-1,0,3,10]
print(sol.sortedSquares(arr))  