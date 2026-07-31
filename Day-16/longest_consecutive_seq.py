# Longest Sequence

# Method - 1 (Brute Force)

class Solution:
    def longest_seq(self, nums: list[int]) -> int:
        n = len(nums)
        max_count = 0
        for i in range(0,n):      #Iterating the array
            num = nums[i]
            count = 1       # The selected element will be starting of the sequence
            while num + 1 in nums:      # If 2 in present in the list, continue iterating
                count += 1             # [1,2] : count = 2
                num += 1                # num = 2
            max_count = max(max_count, count)
        return max_count
            
sol = Solution()
nums = [1,99,101,98,2,5,3,100]
print(sol.longest_seq(nums))


# ---------------------------------

# Method - 2 : (Better Solution)

class Solution:
    def longest_seq(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()    # (1,1,1,2,3,598,99,100,101)
        count = 0
        last_smaller = float("-inf")
        longest = 0
        for i in range(0,n):
            num = nums[i]
            if num-1 == last_smaller:     # If previous number = 0 != -inf, 1 is the starting of new sequence
                count += 1
                last_smaller = num      # last_smaller will be updated in every iteration to check for the next number in sequence
            elif num != last_smaller:      # If last_smaller(previous num) is not 
                count = 1         #reset the counter, new sequence starts
                last_smaller = num
            longest = max(longest, count)
        return longest
            
sol = Solution()
nums = [1,99,101,98,2,5,3,100,1,1]
print(sol.longest_seq(nums))


# ---------------------------------

# Method - 3 : (Optimal Solution) -- *Important*

class Solution:
    def longest_seq(self, nums: list[int]) -> int:
        n = len(nums)
        my_set = set()    # consider a set to solve this problem
        for i in range(0,n):    #Iterate the list and add elements to my_set
            my_set.add(nums[i]) 
        longest = 0
        for num in my_set: 
            if num-1 not in my_set:   # If 0 is in list, what's the point to consider 1 as new sequence, we can just start from 0 as new sequence
                x = num
                count = 1
                while x+1 in my_set:
                    count += 1
                    x += 1
                longest = max(longest, count)
        return longest

sol = Solution()
nums = [1,99,101,98,2,5,3,100,1,1]
print(sol.longest_seq(nums))