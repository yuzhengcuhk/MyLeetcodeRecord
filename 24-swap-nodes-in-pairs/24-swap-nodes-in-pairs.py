# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        leftSwap, rightSwap, remainList = head, head.next, head.next.next
        rightSwap.next = leftSwap
        leftSwap.next = self.swapPairs(remainList)
        return rightSwap
        