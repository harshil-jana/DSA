class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        max_sum = nums[0] + nums[1] + nums[2]

        for i in range(0,n-2):
            j = i + 1
            k = n - 1

            while j < k: 
                total = nums[i] + nums[j] + nums[k]

                if abs(target - total) < abs(target - max_sum):   # For updating the max_sum, based on less difference (closest to target)
                    max_sum = total

                if total < target:
                    j += 1
                elif total == target:
                    return max_sum
                else:
                    k -= 1
                    

        return max_sum

sol = Solution()
nums = [1,1,1,1]
target = 1
print(sol.threeSumClosest(nums, target))