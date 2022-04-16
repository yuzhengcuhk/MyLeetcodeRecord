# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowIndex = head
        fastIndex = head
        while fastIndex and fastIndex.next:
            slowIndex = slowIndex.next
            fastIndex = fastIndex.next.next
        return slowIndex