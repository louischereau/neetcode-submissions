# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        lca = root

        while stack:
            node = stack.pop()

            if p.val <= node.val and q.val >= node.val or q.val <= node.val and p.val >= node.val:
                lca = node
                break
            
            if node.val > p.val and node.val > q.val and node.left:
                stack.append(node.left)

            if node.val < p.val and node.val < q.val and node.right:
                stack.append(node.right)

        return lca