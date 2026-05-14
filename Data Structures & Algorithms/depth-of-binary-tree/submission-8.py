# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        maxHeight = 0
        height = 0

        if not root:
            return maxHeight

        stack = [(root, 1)]

        while stack:
            node, height = stack.pop()
            maxHeight = max(maxHeight, height)
            
            if not node.left and not node.right:
                continue

            if node.left: stack.append((node.left, height + 1))
            if node.right: stack.append((node.right, height + 1))

        return maxHeight

        
        