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

sol = Solution()
s = "aeiou"
k = 2
print(sol.maxVowels(s, k))