class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr1 = []
        arr2 = []

        for i in range(0,2):
            if i == 0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        for i in range(2,n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1+arr2

sol = Solution()
nums = [5,4,3,8]
print(sol.resultArray(nums))