# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        
        mergedList = ListNode()
        startMergedList = mergedList
        
        while list1 and list2:
            if list1.val > list2.val:
                mergedList.next = list2
                list2 = list2.next
            else:
                mergedList.next = list1
                list1 = list1.next

            mergedList = mergedList.next

        if not list2:
            mergedList.next = list1
        else:
             mergedList.next = list2

        return startMergedList.next

    def process_in_pairs(self, items):
        n = len(items)
        interval = 1
        
        while interval < n:
            # Step through the list, jumping by 2 * interval
            for i in range(0, n - interval, interval * 2):
                items[i] = self.mergeTwoLists(items[i], items[i + interval])
                
            # After one full pass, double the distance between pairs
            interval *= 2

        return items[0]
            


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists: return None

        if len(lists) ==  1: return lists[0]

        return self.process_in_pairs(lists)



 




        