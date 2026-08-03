class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        n,m = len(accounts), len(accounts[0])   
        max_count = 0
        sum1 = 0
        for i in range(0,n):
            for j in range(0,m):
                sum1 += accounts[i][j]
            max_count = max(max_count, sum1)
            sum1 = 0
        return max_count

sol = Solution()
nums = [[1,0,1],[1,0,1]]
print(sol.maximumWealth(nums))