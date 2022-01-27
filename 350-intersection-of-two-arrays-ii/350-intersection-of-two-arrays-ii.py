class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        interSet = []
        for item in nums1:
            if item in nums2:
                interSet.append(item)
                nums2.remove(item)
            
        return interSet