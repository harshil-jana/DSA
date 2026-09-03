class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window_set = set()
        
        for i in range(len(nums)):
            if i > k:
                window_set.remove(nums[i - k - 1])
                
            if nums[i] in window_set:
                return True
            
            window_set.add(nums[i])
            
        return False

sol = Solution()
nums = [1,2,3,1]
k = 3
print(sol.containsNearbyDuplicate(nums, k))