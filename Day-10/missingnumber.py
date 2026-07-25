# Find Missing Number

# Method - 1 : Using IN Function - Brute Force

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(0,n+1):
            if i not in nums:
                return i
            
nums = [9,6,4,2,3,5,7,0,1]
sol = Solution()
result = sol.missingNumber(nums)
print(result)

# ----------------------    

# Method - 2 : Better Solution (Dictionary)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        temp = {}
        for i in range(0,n+1):
            temp[i] = 0
        for num in nums:
            temp[num] = 1
        v = 0
        for key, value in temp.items():
            if value == v:
                return key
        
nums = [9,6,4,2,3,5,7,0,1]
sol = Solution()
result = sol.missingNumber(nums)
print(result)


# ----------------------    

# Method - 3 : Optimal Solution (Sum)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        return ((n*(n+1))//2) - sum(nums)
    
nums = [9,6,4,2,3,5,7,0,1]
sol = Solution()
result = sol.missingNumber(nums)
print(result)