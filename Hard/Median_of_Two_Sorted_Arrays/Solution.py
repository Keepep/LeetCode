
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