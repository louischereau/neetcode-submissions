import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        # 1. Use a simple pointer/reference 'current' instead of deep copy
        current = self 
        
        while current is not None:
            values.append(current.val)
            current = current.next
            
        # 2. Return the string representation of the list, do not print it.
        return str(values)




class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev, curr = None, head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def splitListInMiddle(self, head: Optional[ListNode]) -> List[Optional[ListNode], Optional[ListNode]]:
        
        slow, fast = head, head 

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        list1 = head
        list2 = slow.next
        slow.next = None

        return [list1, list2]

    def reorderList(self, head: Optional[ListNode]) -> None:

        list1, list2 = self.splitListInMiddle(head)

        list2 = self.reverseList(list2)

        # make sure list2.length < list1.length
        while list2:
            
            next1, next2 = list1.next, list2.next
            
            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2
        
        return
        
        