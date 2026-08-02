class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []

        for i in range(0,n):
            ans.append(nums[nums[i]])
        return ans

sol = Solution()
arr = [1,2,1]    # Array should contain numbers ranging (0 to n-1)
result = sol.buildArray(arr)
print(result)