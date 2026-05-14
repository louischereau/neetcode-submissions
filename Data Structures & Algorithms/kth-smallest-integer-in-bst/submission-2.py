# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)

        values = inorderTraversal(root)
        return values[k - 1]
        