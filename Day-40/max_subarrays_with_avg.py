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
    
sol = Solution()
arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
print(sol.numOfSubarrays(arr, k, threshold))

    