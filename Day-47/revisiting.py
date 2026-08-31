class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_sum = 0
        current_sum = 0
        left = 0
        freq = {}

        for right in range(0,n):
            current_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if right - left + 1 > k:
                current_sum -= nums[left]
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1
            
            if right - left + 1 == k:
                if len(freq) == k:
                    max_sum = max(current_sum, max_sum)

        return max_sum

sol = Solution()
arr = [1,2,3,4,4,2]
k = 3
print(sol.maximumSubarraySum(arr, k))