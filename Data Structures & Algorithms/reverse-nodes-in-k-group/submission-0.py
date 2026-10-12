class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        def has_k(node):
            for _ in range(k):
                if not node:
                    return False
                node = node.next
            return True

        k_group_head = head
        new_head = None
        prev_tail = None

        while has_k(k_group_head):
            l, r = k_group_head, k_group_head.next

            for _ in range(k - 1):
                temp = r.next
                r.next = l
                l = r
                r = temp

            if new_head is None:
                new_head = l
            else:
                prev_tail.next = l      # link previous group's tail to this group's new head

            k_group_head.next = r       # this group's tail points to the rest (fixed up next loop if reversed)
            prev_tail = k_group_head
            k_group_head = r

        return new_head or head