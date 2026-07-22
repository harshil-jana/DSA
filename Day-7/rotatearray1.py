#Rotate Array Right by One Place 

class Solution:
    def rotatearray(self, nums):
        n = len(nums)
        temp = nums[n-1]       #We store the last digit in a temporary variable initially.

        for i in range(n-2,-1,-1):      #We right shift the numbers from left to right (5th index to 0)
            nums[i+1] = nums[i]     
        nums[0] = temp      #The first position is the temp variable.
 
        return nums

nums = [1,2,4,5,2,-3]
sol = Solution()
result = sol.rotatearray(nums)
print(result)