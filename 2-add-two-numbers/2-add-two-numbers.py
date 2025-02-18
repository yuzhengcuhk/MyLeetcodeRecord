# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curNode = dummy
        carry = 0
        while l1 or l2 or carry:
            add1 = l1.val if l1 else 0
            add2 = l2.val if l2 else 0
            addRes = add1 + add2 + carry 
            carry = 1 if addRes >= 10 else 0
            addRes = addRes - 10 if carry else addRes
            curNode.next = ListNode(addRes)
            curNode = curNode.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
        