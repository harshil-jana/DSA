class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0
        running_sum = []

        for num in nums:
            sum += num
            running_sum.append(sum)
        return running_sum

sol = Solution()
arr = [1,2,3]
result = sol.runningSum(arr)
print(result)