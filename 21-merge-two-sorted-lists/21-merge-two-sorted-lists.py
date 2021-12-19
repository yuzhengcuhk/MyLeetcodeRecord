# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        linklist= ListNode()
        merge=linklist
        while  l1 and l2:
            if l1.val <l2.val:
                merge.next = l1
                l1 = l1.next
            else:
                merge.next = l2
                l2 = l2.next
            merge = merge.next
        while l1:
            merge.next = l1
            l1  = l1.next
            merge = merge.next
        while l2:
            merge.next = l2
            l2  = l2.next
            merge = merge.next
        return(linklist.next)