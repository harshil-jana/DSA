# Remove Element from Array (Two Pointers)

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        i = 0
        for j in range(0,n):
            if nums[j] != val:
                nums[j], nums[i] =  nums[i], nums[j]
                i += 1
        return i    
        

sol = Solution()
arr = [3,2,2,3]
k = 3
print(sol.removeElement(arr,k))  
