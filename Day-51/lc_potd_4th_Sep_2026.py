class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(0,n):
            max_num = max(nums[0:i+1])
            min_num = min(nums[i:n])
            if max_num - min_num <= k:
                return i
        return -1

sol = Solution()
nums = [5,0,1,4]
k = 3
print(sol.firstStableIndex(nums, k))    