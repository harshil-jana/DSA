# Largest Element

class Solution:
    def largestElement(self, nums):
        largest = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > largest:
                largest = nums[i]
        return largest

sol = Solution()
arr = [1,2,4,7,9]
result = sol.largestElement(arr)
print(f"The largest element is {result}")


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

# class Solution:
#     def largestElement(self, nums, n):
#         if n == 0 or n == 1:
#             return -1

#         small = float("inf")        
#         second_s = float("inf")        
#         large = float("-inf")        
#         second_l = float("-inf")        

#         for i in range(n):
#             small = min(small, arr[i])  
#             large = max(large, arr[i]) 

#         for i in range(n):
#             if arr[i] < second_s and arr[i] != small:
#                 second_s = arr[i]
#             if arr[i] > second_l and arr[i] != large:
#                 second_l = arr[i]

#         return second_s
#         return second_l

            


# sol = Solution()
# arr = [1,2,10,4,9]
# result = sol.largestElement(arr, 5)
# print(result)

