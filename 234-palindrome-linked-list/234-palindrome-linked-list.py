# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slowIndex, fastIndex = head, head
        while fastIndex and fastIndex.next:
            fastIndex = fastIndex.next.next
            slowIndex = slowIndex.next
        
        reverSecHalf = None
        currentNode = slowIndex
        while currentNode:
            tempNode = currentNode.next
            currentNode.next = reverSecHalf
            reverSecHalf = currentNode
            currentNode = tempNode
        
        firstNode = head
        secondNode = reverSecHalf
        while secondNode:
            if firstNode.val != secondNode.val:
                return False
            firstNode = firstNode.next
            secondNode = secondNode.next
            
        return True
            