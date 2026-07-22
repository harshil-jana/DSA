# Rotate Array by k places

# Method - 1

class Solution:
    def rotatenumsayk(self, nums: list[int], k: int) -> None:
        n = len(nums)
        temp = {}

        for i in range(n-k, n):
            temp[nums[i]] = 0

        for i in range(n-k-1, -1, -1):
            nums[i+k] = nums[i]

        j = 0

        for key in temp:
            nums[j] = key
            j += 1

        return nums

nums = [5,-2,3,9,0,6,10,7]
sol = Solution()
result = sol.rotatenumsayk(nums, 1)
print(result)


# -------------------------

# Method - 2

class Solution:
    def rotatenumsayk(self, nums: list[int], k: int) -> None:
        n = len(nums)
        rotations = k % n

        for _ in range(0,rotations):
            e = nums.pop()
            nums.insert(0,e)

        return nums

nums = [5,-2,3,9,0,6,10,7]
sol = Solution()
result = sol.rotatenumsayk(nums, 3)
print(result)


# ---------------------------

# Method - 3

class Solution:
    def rotatenumsayk(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums[:] = nums[n-k:] + nums[:n-k]

        return nums

nums = [5,-2,3,9,0,6,10,7]
sol = Solution()
result = sol.rotatenumsayk(nums, 3)
print(result)


# ---------------------------

# Method - 4 (Two Pointers)

class Solution:
    def reverse(self, nums: list[int], left = int, right = int) -> None:

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate (self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n      #Handle cases where k might be larger than n (k > 10)

        self.reverse(nums, n-k, n-1)    #Reverse the last k elements
        self.reverse(nums, 0,n-k-1)     #Reverse first n-k elements
        self.reverse(nums, 0,n-1)       #Reverse the entire array

        return nums

nums = [5,-2,3,9,0,6,10,7]
sol = Solution()
result = sol.rotate(nums,5)
print(result)