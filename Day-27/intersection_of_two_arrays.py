# Intersection of Two Arrays

# Method - 1 (Hashmap)

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashmap = {}
        result = []

        for num in nums1:
            hashmap[num] = 1
        for num in nums2:
            if num in hashmap and hashmap[num] == 1:
                result.append(num)
                hashmap[num] = 2
        return result

nums1 = [2,3,4,2]
nums2 = [1,2,3,4]
sol = Solution()
print(sol.intersection(nums1, nums2))

