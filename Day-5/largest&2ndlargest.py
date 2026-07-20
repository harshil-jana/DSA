#Largest Element

# class Solution:
#     def largestElement(self, nums):
#         largest = nums[0]
#         for i in range(1,len(nums)):
#             if nums[i] > largest:
#                 largest = nums[i]
#         return largest

# sol = Solution()
# arr = [1,2,4,7,9]
# result = sol.largestElement(arr)
# print(result)


#Second Largest Element

#1st Method

# class Solution:
#     def largestElement(self, nums):
#         sorted_nums = nums.sort()

#         return nums[-1]

# sol = Solution()
# arr = [1,2,10,4,9]
# result = sol.largestElement(arr)
# print(result)


#2nd Method

class Solution:
    def largestElement(self, nums, n):
        if n == 0 or n == 1:
            return -1
        

        return nums[-1]

sol = Solution()
arr = [1,2,10,4,9]
result = sol.largestElement(arr)
print(result)

