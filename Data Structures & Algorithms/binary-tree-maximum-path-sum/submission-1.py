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

            # This calculates a path that comes up from the left subtree, passes through the current node, and goes down into the right subtree. If you are at node C and you use both your left child and your right child to form a peak, you have used C as a "turning point." A parent node above C cannot connect to this path because doing so would require visiting C twice (or creating a fork/loop), which violates the definition of a simple path.
            current_path = node.val + maxLeft + maxRight

            maxSum = max(maxSum, current_path)

            # This calculates the best single-direction path extending upward through the current node. When the parent node asks the current node for its contribution, the parent can only extend a path down one branch (either the left child or the right child, whichever is larger). It cannot split and go down both.
            return node.val + max(maxLeft, maxRight)

        dp(root)

        return maxSum