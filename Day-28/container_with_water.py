class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1

        while i < j:
            if height[i] < height[j]:
                area = (j-i) * min(height[j], height[i])
                max_area = max(max_area, area)
                i += 1
            else:
                area = (j-i) * min(height[j], height[i])
                max_area = max(max_area, area)
                j -= 1
        return max_area

sol = Solution()
nums = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(nums))