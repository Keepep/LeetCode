"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        lenNum1=len(nums1)
        lenNum2=len(nums2)

        if lenNum1>lenNum2:
            tmpResult=nums1
            tmplen=lenNum2
            tmpInsert=nums2
        else:
            tmpResult=nums2
            tmplen=lenNum1
            tmpInsert=nums1

        #saveIndex for reducing the number of compr elements in tmpResult
        saveIndex=0
        for i in range (tmplen):

            #lowerBound is to search an index of tmpInsert[i] that will be inserted in the tmpResult
            insertIndex=self.lowerBound(tmpInsert[i],tmpResult[saveIndex:])
            if tmpInsert[i]>tmpResult[-1]:
                insertIndex+=1
            tmpResult.insert(insertIndex+saveIndex,tmpInsert[i])
            saveIndex=insertIndex

        #if total length of lists is a even number
        if (lenNum1+lenNum2) %2 ==0:
            return (tmpResult[(lenNum1+lenNum2)//2]+tmpResult[(lenNum1+lenNum2)//2-1])/2

        else:
            return tmpResult[(lenNum1+lenNum2)//2]
    def lowerBound(self,ob: int, comp: list):
        first = 0
        last = len(comp) - 1
        while last > first:
            mid = (first + last) // 2

            if ob >= comp[mid]:
                first = mid+1
            elif ob < comp[mid]:
                last = mid

        return last