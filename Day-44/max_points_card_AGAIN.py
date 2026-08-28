class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        l = 0
        r = n - k
        current_sum = sum(cardPoints[r:])
        max_sum = current_sum

        for i in range(0,k):
            current_sum = current_sum - cardPoints[n-k+i] + cardPoints[l]
            max_sum = max(max_sum, current_sum)
            l += 1

        return max_sum

sol = Solution()
nums = [2,2,2]
k = 2   
print(sol.maxScore(nums, k))