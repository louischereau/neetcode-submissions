# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")

        def dp(node: Optional[TreeNode]):
            nonlocal maxSum

            if not node:
                return 0
            
            maxLeft = max(0, dp(node.left))
            maxRight = max(0, dp(node.right))

            current_path = node.val + maxLeft + maxRight

            maxSum = max(maxSum, current_path)

            return node.val + max(maxLeft, maxRight)

        dp(root)

        return maxSum