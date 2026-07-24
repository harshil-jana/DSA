# Merge Sorted Arrays (With Duplicates)

def merge2sarrays(left, right):
    result = []
    i,j = 0,0
    n,m = len(left), len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    if i < n:
        while i < n:
            result.append(left[i])
            i+=1
    if j < m:
        while j < m:
            result.append(right[j])
            j+=1

    return result

left = [1,2,2,3,4]
right = [1,2,4,6,8]
final_list = merge2sarrays(left,right)
print(final_list)


# ----------------------------

# Merge Sorted Arrays (Without Duplicates)

def merge2sarrays(nums1, nums2):
    result = []
    i,j = 0,0
    n,m = len(nums1), len(nums2)

    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i+=1
        else:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j+=1

    if i < n:
        while i < n:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i+=1
    if j < m:
        while j < m:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j+=1
    
    return result

left = []
right = []
final_list = merge2sarrays(left,right)
print(final_list)

