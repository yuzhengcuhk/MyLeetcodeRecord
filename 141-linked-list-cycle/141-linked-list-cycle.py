# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            nodeP1 = head
            nodeP2 = head.next
        else:
            nodeP1 = None
            nodeP2 = None            
            
        while nodeP1 != None and nodeP2 != None and nodeP2.next != None:
            if nodeP1 == nodeP2:
                return True
            else:
                nodeP1 = nodeP1.next
                nodeP2 = nodeP2.next.next
        return False
        