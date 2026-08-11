# Two Sum II - Input Array is Sorted

# Method - 1 (Two Pointers)

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        low = 0
        high = n-1

        while low < high:
            if numbers[low] + numbers[high] == target:
                return [low + 1, high + 1]
            elif numbers[low] + numbers[high] > target:
                high -= 1
            else:
                low += 1

sol = Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums, target))


# ---------------------------------

# Method - 2 (Using HashMap)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        hash_map = {}
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [hash_map[remaining] + 1, i + 1]
            hash_map[nums[i]] = i

sol = Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums, target))