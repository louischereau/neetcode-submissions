# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Create a dummy node to act as the head of the merged list.
        # This prevents edge cases with an empty merged list.
        head = ListNode()

        # 2. Create a pointer 'tail' that will always point to the last 
        # node of the merged list (or the dummy node initially).        
        tail = head

        # 3. Loop while both lists have nodes.
        while list2 is not None and list1 is not None:

            if list2.val >= list1.val:
                # Attach the smaller node (from list1) to the current tail.
                tail.next = list1
                # Advance list1 to its next node.
                list1 = list1.next
            else:
                # Attach the smaller node (from list2) to the current tail.
                tail.next = list2
                # Advance list2 to its next node.
                list2 = list2.next

            # Move the tail pointer forward to the newly added node.
            tail = tail.next

        # 4. Handle remaining nodes (one list might still have elements).
        # We only need to check one of them, as the other will be None.
        if list1 is None:
            tail.next = list2
        
        if list2 is None:
            tail.next = list1
        
        return head.next



        