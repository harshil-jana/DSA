class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        n = len(nums)
        main_count = 0
        for i in range(0,n):
            temp = nums[i]
            count = 0
            while temp != 0:
                count += 1
                temp //= 10
            if count % 2 == 0:
                main_count += 1
        return main_count

sol = Solution()
nums = [1,0,1,1,0,1]
print(sol.findNumbers(nums))