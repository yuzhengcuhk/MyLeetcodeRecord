class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        
        iLeftIndex, iRightIndex, halfLength = 0, m, (m+n+1)//2 
        while iLeftIndex <= iRightIndex:
            i = (iLeftIndex + iRightIndex) // 2
            j = halfLength - i
            if i < m and nums2[j-1] > nums1[i]:
                iLeftIndex = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                iRightIndex = i - 1
            else:
                if i == 0:
                    maxLeftNums = nums2[j-1]
                elif j == 0:
                    maxLeftNums = nums1[i-1]
                else: 
                    maxLeftNums = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2 == 1:
                    return maxLeftNums
                if i == m:
                    minRightNums = nums2[j]
                elif j == n:
                    minRightNums = nums1[i]
                else:
                    minRightNums = min(nums1[i], nums2[j])
                return (maxLeftNums + minRightNums) / 2 
            