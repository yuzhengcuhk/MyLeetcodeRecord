# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        while current_node is not None and current_node.next is not None:
            next_node = current_node.next
            while next_node is not None and next_node.val == current_node.val:
                next_node = next_node.next
            current_node.next = next_node
            current_node = next_node
        return head