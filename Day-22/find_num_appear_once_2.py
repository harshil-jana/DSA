# Find Number Which Appears Once

# Method - 2 (HashMap)

class Solution:
    def findNumappearOne(self, arr: list[int]) -> int:
        hash_map = {}
        n = len(arr)
        for  i in range(0,n):
            hash_map[arr[i]] = 0

        for num in arr:
            hash_map[num] += 1

        for key in hash_map:
            if hash_map[key] == 1:
                return key
        return -1
    
sol = Solution()
arr = [2,2,1]
print(sol.findNumappearOne(arr))          


# -------------------------------------------

# Method - 3 (XOR)

class Solution:
    def getSingleElement(self, arr):
        xorr = 0

        for num in arr:
            xorr ^= num    # XOR = Duplicates cancel out

        return xorr
    
sol = Solution()
arr = [2,2,1]
print(sol.findNumappearOne(arr))          


