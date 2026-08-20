class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = 0
        avg = 0
        max_avg = float("-inf")
        n = len(nums)

        if n == 1:
            return nums[0]

        for i in range(0,k):
            total += nums[i]
        avg = total/k
        max_avg = max(max_avg, avg)

        if k == n:
            return max_avg

        i = 1
        j = k

        while j < n:
            total = total + nums[j] - nums[i-1]
            avg = total/k
            max_avg = max(max_avg, avg)
            i += 1
            j += 1

        return max_avg

nums = [8819, 674, 8816, 7705, 5699, 5383, 6177, 2113, 1992]
k = 4
print(Solution().findMaxAverage(nums, k))