# Sort Colors (0's, 1's, 2's)

# Method - 1 (Count Approach)

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        c1 = 0
        c2 = 0
        c3 = 0
        for i in range(0,n):
            if nums[i] == 0:
                c1 += 1
            elif nums[i] == 1:
                c2 += 1
            else:
                c3 += 1

        j = 0
        for i in range(0,c1):
            nums[j] = 0
            j += 1
        for i in range(0,c2):
            nums[j] = 1
            j += 1
        for i in range(0,c3):
            nums[j] = 2
            j += 1

        return nums

nums = [2,0,2,1,1,0]
print(Solution().sortColors(nums))


# ----------------------------------------

# Method - 2 (Three Pointers)

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        low = 0
        curr = 0
        high = n - 1

        while curr <= high: 
            if nums[curr] == 2:   # For 2's at higher indices
                nums[curr], nums[high] = nums[high], nums[curr]
                high -= 1
            elif nums[curr] == 0:  # For 0's at lower indices
                nums[curr], nums[low] = nums[low], nums[curr]
                low += 1
                curr += 1
            else:   # For 1's
                curr += 1

        return nums

nums = [2,0,2,1,1,0]
print(Solution().sortColors(nums))