class Solution:
    def maxSubarraySum(self, arr, k):
        total = 0
        max_sum = 0
        n = len(arr)

        for i in range(0,k):
            total += arr[i]
            max_sum = max(max_sum, total)

        if k == n:
            return total

        i = 1
        j = k

        while j < n:
            total = total + arr[j] - arr[i-1]
            max_sum = max(max_sum, total)
            i += 1
            j += 1

        return max_sum

nums = [8819, 674, 8816, 7705, 5699, 5383, 6177, 2113, 1992]
k = 1 
print(Solution().maxSubarraySum(nums, k))