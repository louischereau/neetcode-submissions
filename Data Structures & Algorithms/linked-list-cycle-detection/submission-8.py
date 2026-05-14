# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        curr, post = head, head.next
        while post is not None:
            if post.val == 1001:
                return True
            curr.val = 1001
            curr = curr.next
            post = post.next
        return False

        