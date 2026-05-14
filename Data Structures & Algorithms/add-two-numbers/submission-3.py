# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = ""
        number2 = ""

        curr1 = l1

        curr2 = l2

        while curr1 or curr2:
            if curr1:
                number1 = str(curr1.val) + number1
                curr1 = curr1.next
            
            if curr2:
                number2 = str(curr2.val) + number2
                curr2 = curr2.next

        number = str(int(number1) + int(number2))

        l = ListNode(number[-1])
        prev = l

        for i in range(len(number) - 2, -1, -1):
            node = ListNode(number[i])
            prev.next = node
            prev = node
            
        return l
        