# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        queue = deque([root])

        heap = []

        while queue:
            node = queue.popleft()
            heap.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        heapq.heapify(heap)

        return heapq.nsmallest(k, heap)[-1]
        




        
        