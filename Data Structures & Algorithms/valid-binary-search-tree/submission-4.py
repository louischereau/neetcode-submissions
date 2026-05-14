# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -math.inf, math.inf)]

        while stack:
            node, mini, maxi = stack.pop()

            if not mini < node.val < maxi: return False

            # 2. Add right child: must be > current val, but < current high
            if node.right:
                stack.append((node.right, node.val, maxi))
                
            # 3. Add left child: must be < current val, but > current low
            if node.left:
                stack.append((node.left, mini, node.val))

        return True
        


