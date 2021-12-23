# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        currentNode = head
        while currentNode:
            nextTempStore = currentNode.next
            currentNode.next = result
            result = currentNode
            currentNode = nextTempStore
        
        return result
        