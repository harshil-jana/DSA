class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0 for _ in range(2*n)]

        for i in range(0,n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]

        return ans

sol = Solution()
arr = [1,2,3]
result = sol.getConcatenation(arr)
print(result)