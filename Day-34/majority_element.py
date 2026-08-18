class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        hashmap = {}

        for i in range(0,n):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        j = 0
        for key in hashmap:
            if hashmap[key] > n//2:
                return key
            j += 1



nums = [0,2,0]
print(Solution().majorityElement(nums))