class Solution:
    def maxSubarraySum(self, nums, k):
        total = 0
        max_sum = 0
        n = len(nums)

        for i in range(0,k):
            total += nums[i]
            max_sum = max(max_sum, total)

        if k == n:
            return total

        i = 1
        j = k

        while j < n:
            total = total + nums[j] - nums[i-1]
            max_sum = max(max_sum, total)
            i += 1
            j += 1

        return max_sum

nums = [8819, 674, 8816, 7705, 5699, 5383, 6177, 2113, 1992]
k = 1 
print(Solution().maxSubnumsaySum(nums, k))