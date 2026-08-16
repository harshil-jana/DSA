class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        i = 0
        j = i+1
        total = 0
        max_num = max(height)

        while j < n: 
            if i > 1 and height[i] == max_num:
                i += 1
                j += 1
            elif height[i] == 0:
                i += 1
                j += 1
            else:
                if height[j] < height[i]:
                    total += abs(height[j] - height[i])
                    j += 1
                elif height[j] == height[i]:
                    i += 1
                    j += 1
                else:
                    i = j
                    j += 1
        
        return total

height = [0,2,0]
print(Solution().trap(height))
        