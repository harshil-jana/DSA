Reverse of an array 

class Solution:    #First Solution
    def reverse(self, arr: list) -> None:
        n = len(arr)
        mid = n // 2
        for i in range(0,mid):
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
            
        return arr

result = Solution()
print(result.reverse(arr = [1,2,1,1,5,1]))


class Solution:    #Two Pointers Method
    def reverse(self, arr: list) -> None:
        n = len(arr)
        left = 0
        right = n-1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

result = Solution()
print(result.reverse(arr = [1,2,3,4,5]))


# -------------------

class Solution:     #Two Pointers with Strings
    def reverse(self, arr: list) -> None:
        n = len(arr)
        left = 0
        right = n-1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

result = Solution()
print(result.reverse(arr = ["s", "t", "r", "i", "n", "g"]))
