# Trapping Rain Water 

# Two Pointers

class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height)-1
        left_max, right_max = 0, 0
        total_units = 0

        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            
            if left_max < right_max:
                total_units += left_max - height[l]
                l += 1
            else:
                total_units += right_max - height[r]
                r -= 1
        return total_units