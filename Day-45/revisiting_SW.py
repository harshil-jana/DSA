# 𝐌𝐚𝐱𝐢𝐦𝐮𝐦 𝐒𝐮𝐦 𝐒𝐮𝐛𝐚𝐫𝐫𝐚𝐲 𝐨𝐟 𝐒𝐢𝐳𝐞 𝐊

class Solution:
    def maxSubarraySum(self, arr, k):
        total = 0
        max_sum = 0
        n = len(arr)
    
        for i in range(0,k):
            total += arr[i]
            max_sum = max(max_sum, total)
    
        if k == n:
            return total
    
        i = 1
        j = k
    
        while j < n:
            total = total + arr[j] - arr[i-1]
            max_sum = max(max_sum, total)
            i += 1
            j += 1
    
        return max_sum

# ------------------------------------------

# 𝐌𝐚𝐱𝐢𝐦𝐮𝐦 𝐀𝐯𝐞𝐫𝐚𝐠𝐞 𝐒𝐮𝐛𝐚𝐫𝐫𝐚𝐲 𝐈

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = 0
        avg = 0
        max_avg = float("-inf")
        n = len(nums)

        if n == 1:
            return nums[0]

        for i in range(0,k):
            total += nums[i]
        avg = total/k
        max_avg = max(max_avg, avg)

        if k == n:
            return max_avg

        i = 1
        j = k

        while j < n:
            total = total + nums[j] - nums[i-1]
            avg = total/k
            max_avg = max(max_avg, avg)
            i += 1
            j += 1

        return max_avg

# ---------------------------------------------

# 𝐍𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐒𝐮𝐛-𝐚𝐫𝐫𝐚𝐲𝐬 𝐨𝐟 𝐒𝐢𝐳𝐞 𝐊 𝐚𝐧𝐝 𝐀𝐯𝐞𝐫𝐚𝐠𝐞 ≥ 𝐓𝐡𝐫𝐞𝐬𝐡𝐨𝐥𝐝

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        n = len(arr)
        count = 0
        total = 0

        if n == 1:
            return arr[0]
        for i in range(0,k):
            total += arr[i]

        avg = total/k
        if avg >= threshold:
            count += 1

        if k == n:
            return count

        i = 1
        j = k

        while j < n:
            total = total + arr[j] - arr[i-1]
            avg = total/k
            if avg >= threshold:
                count += 1
            i += 1
            j += 1

        return count

nums = [8819, 674, 8816, 7705, 5699, 5383, 6177, 2113, 1992]
k = 1 
print(Solution().numOfSubarrays(nums, k))