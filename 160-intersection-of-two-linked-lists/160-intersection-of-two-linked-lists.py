# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        nodeA = headA
        nodeB = headB
        cntA = 0
        cntB = 0
        
        while nodeA:
            nodeA = nodeA.next
            cntA = cntA + 1
        while nodeB:
            nodeB = nodeB.next
            cntB = cntB + 1
        
        diff = abs(cntA - cntB)
        
        if cntA >= cntB:
            while diff:
                headA = headA.next
                diff = diff - 1
        elif cntA < cntB:
            while diff:
                headB = headB.next
                diff = diff - 1
                
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
   
