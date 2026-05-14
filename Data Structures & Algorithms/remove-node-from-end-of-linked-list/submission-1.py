# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        curr = self
        while curr:
            values.append(curr.val)
            curr = curr.next
        return str(values)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        reversed_head = self.reverseList(head)
        reversed_list = reversed_head

        if n == 1:
            target = reversed_list
            reversed_list = reversed_list.next
            reversed_head = reversed_list
            target.next = None
            return self.reverseList(reversed_head)

        for _ in range(1, n - 1):
            reversed_list = reversed_list.next
            
        target = reversed_list.next

        if target:
            reversed_list.next = reversed_list.next.next
            target.next = None

        return self.reverseList(reversed_head)

        

        

            