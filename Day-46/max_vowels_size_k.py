# Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        max_sum = 0
        vowels = "aeiou"
        count = 0

        for i in range(0,k):
            if s[i] in vowels:
                count += 1
        max_sum = count

        for i in range(k, n):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            max_sum = max(max_sum, count)
        return max_sum

nums = [8819, 674, 8816, 7705, 5699, 5383, 6177, 2113, 1992]
k = 1 
print(Solution().maxVowels(nums, k))