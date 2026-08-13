class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        nums.sort()

        for i in range(0,n-2):
            j = i + 1
            k = n - 1
            if i > 0 and nums[i] == nums[i - 1]:   # Duplicate checking for i
                continue
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    result.append([nums[i],nums[j],nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1

        return result
            
sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))