class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        interSet = []
        for item in nums1:
            if item in nums2 and item not in interSet:
                interSet.append(item)
            
        return interSet