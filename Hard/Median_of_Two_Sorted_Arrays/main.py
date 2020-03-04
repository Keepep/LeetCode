from Hard.Median_of_Two_Sorted_Arrays.Solution import Solution


if __name__ == "__main__":
    nums1= [1,3,9,10,400]
    nums2= [0,2,4,5,6,7,8,1000,2000]

    sol=Solution()

    print(sol.findMedianSortedArrays(nums1,nums2))