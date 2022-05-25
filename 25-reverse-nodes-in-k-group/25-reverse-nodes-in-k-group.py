# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or (k <= 1):
            return head
        countK = 0
        currNode = head
        while currNode:
            countK += 1
            if countK == k:
                break
            currNode = currNode.next
        if countK < k:
            return head
        nextHead = currNode.next
        leftIndex, rightIndex = ListNode(0), ListNode(0)
        currNode = head
        for i in range(0, k):
            rightIndex = currNode.next
            currNode.next = leftIndex
            leftIndex = currNode
            currNode = rightIndex
        head.next = self.reverseKGroup(nextHead, k)
        return leftIndex
            
        