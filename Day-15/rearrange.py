class Solution:
    def rearrange(self, arr: list[int]) -> list[int]:
        n = len(arr)
        pos, neg = 0,1
        result = [0] * n
        for i in range(0,n):
            if arr[i] > 0:
                result[pos] = arr[i]
                pos += 2
            else:
                result[neg] = arr[i]
                neg += 2

        return result

sol = Solution()
arr = [5,10,-3,-1,-10,6]
print(sol.rearrange(arr))