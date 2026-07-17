class Solution:    #Time complexity = O(n^2)
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        flag = False
        for i in range(0,n):        #Iterating i
            for j in range(i+1,n):    #Iterating i with the remaining elements
                if nums[i] == nums[j]:
                    flag = True
                    break
        if flag:
            return True
        else:
            return False
        

# -------------------------

class Solution:    #Time complexity = O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()    #Storing in the hashset  

        for num in nums:
            if num in num_set:  #If adding element is already present in the set, return True.
                return True
            num_set.add(num)    #Adding each element 
        return False

         