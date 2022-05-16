# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(0)
        root.next = head
        fastIndex, slowIndex, preIndex = root, root, root
        while n - 1 > 0:
            fastIndex = fastIndex.next
            n -= 1
        while fastIndex.next:
            fastIndex = fastIndex.next
            preIndex = slowIndex
            slowIndex = slowIndex.next
        preIndex.next = slowIndex.next
        return root.next
            