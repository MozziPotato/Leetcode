class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        mergedlist = list()
        
        j = len(nums1)
        k = len(nums2)
        
        m = 0
        n = 0
        
        while m < j or n < k:
            
            if m < j and n < k:
                if nums1[m] <= nums2[n]:
                    mergedlist.append(nums1[m])
                    m += 1
                else:
                    mergedlist.append(nums2[n])
                    n += 1
            
            elif m < j:
                mergedlist.append(nums1[m])
                m += 1
            
            else:
                mergedlist.append(nums2[n])
                n += 1
        
        length = len(mergedlist)
        
        if length%2 == 1:
            return mergedlist[length//2]
        else:
            return (mergedlist[length//2-1] + mergedlist[length//2])/2
        
        return mergedlist
    
    def mergeSort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        
        return mergedlist