"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        curr_copy = Node(head.val)
        head_copy = curr_copy
        curr = head.next

        cache = {}

        cache[head] = head_copy

        while curr:
            copy = Node(curr.val)
            cache[curr] = copy
            curr_copy.next = copy
            curr = curr.next
            curr_copy = curr_copy.next 

        curr = head
        curr_copy = head_copy

        while curr:
            curr_copy.random = cache[curr.random] if curr.random in cache else None
            curr_copy = curr_copy.next
            curr = curr.next

        return head_copy

        
        
        