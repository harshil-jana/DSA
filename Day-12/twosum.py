# Two Sum

# Method - 1 (Brute Force)

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)    
                    return result

sol = Solution()
nums = [2,4,5,3,0]
target = 5
print(sol.two_sum(nums, target))


# -----------------------------

# Method - 2 (Optimal Approach)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        hash_map = {}
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [hash_map[remaining], i]
            hash_map[nums[i]] = i

sol = Solution()
nums = [2,4,5,3,0]
target = 5
print(sol.twoSum(nums, target))