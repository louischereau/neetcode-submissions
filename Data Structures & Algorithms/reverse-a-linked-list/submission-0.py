# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousNode = None
        nextNode = None
        if head is None:
            return head
        while head is not None:
            nextNode = head.next
            head.next = previousNode
            previousNode = head
            head = nextNode
        return previousNode


        