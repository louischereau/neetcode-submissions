# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height(node):
            if not node:
                return 0
            
            left_height = get_height(node.left)

            # If the left subtree is already unbalanced, propagate the -1
            if left_height == -1: return -1

            right_height = get_height(node.right)

            # If the right subtree is already unbalanced, propagate the -1
            if right_height == -1: return -1

            if abs(right_height - left_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        res = get_height(root)

        return True if res >= 0 else False

        