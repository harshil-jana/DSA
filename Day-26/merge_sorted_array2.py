class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i,j = 0,0
        result = []

        while i < m and j < n:     
            if nums1[i] <= nums2[j]:        # Compare and push into the new array
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        while i < m:          # If j list gets exhausted, the remaining elements in i list gets pushed into the new array
            result.append(nums1[i])
            i += 1
        while j < n:          # If i list gets exhausted, the remaining elements in j list gets pushed into the new array
            result.append(nums2[j])
            j += 1
        for k in range(m+n):   #As the nums1 array has the length m + n and the result to be stored in nums1, we run a loop to insert the result array elements into nums1 array
            nums1[k] = result[k]


nums1 = [0]
m = 0
nums2 = [1]
n = 1
sol = Solution()
print(sol.merge(nums1, m, nums2, n))

