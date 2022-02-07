class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for item in nums1:
            if item in nums2:
                indexItem = nums2.index(item)
                indexNext = indexItem + 1
                while indexNext < len(nums2):
                    if nums2[indexNext] > nums2[indexItem]:
                        result.append(nums2[indexNext])
                        break
                    else:
                        indexNext += 1
                if indexNext == len(nums2):
                    result.append(-1)
        return result
                        
                