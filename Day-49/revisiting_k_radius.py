class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        windowSize = 2 * k + 1

        windowSum = 0
        result = [-1] * n

        if n < windowSize:
            return result

        for i in range(n):
            windowSum += nums[i]  

            if i - windowSize >= 0:
                windowSum -= nums[i - windowSize]  

            if i >= windowSize - 1:
                result[i - k] = windowSum // windowSize  

        return result

sol = Solution()
nums = [7,4,3,9,1,8,5,2,6]
k = 3
print(sol.getAverages(nums, k))