class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftside = self.modified_binary(nums, target, True)   #For the starting position, we check the left side.
        rightside = self.modified_binary(nums, target, False)  #For the ending position, we check the right side.
        return [leftside, rightside]


    def modified_binary(arr, target, leftbias):     #leftbias = True (if target is on the left from mid position)
        n = len(arr)                                #leftbias = False (if target is on the right from mid positions)
        start = 0
        end = n-1
        i = -1
        
        while (start<=end):
            mid = (start + end)//2
            if arr[mid] < target:
                start = mid+1
            elif arr[mid] > target:
                end = mid-1
            else:
                i = mid
                if leftbias:
                    end = n-1
                else:
                    start = n+1

        return i







        