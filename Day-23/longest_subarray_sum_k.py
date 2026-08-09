# Longest Subarray with Sum K

class Solution:
    def longestSubarray(self, arr, k):  
        n = len(arr)
        max_len = 0
        prefix_map = {0:-1} 
        prefix_sum = 0
        
        for i in range(0,n):
            prefix_sum += arr[i]
            previous_prefix = prefix_sum - k
            if previous_prefix in prefix_map:
                length = i - prefix_map[previous_prefix]
                max_len = max(max_len, length)
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
        return max_len                       

sol = Solution()
arr = [10,5,2,7,1,-10]
k = 15
print(sol.longestSubarray(arr,k))  


