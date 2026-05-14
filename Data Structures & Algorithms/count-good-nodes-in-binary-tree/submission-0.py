# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        result = [root]

        while stack:
            node, max_val = stack.pop()
            if node.left:
                if node.left.val >= max_val:
                    stack.append((node.left, node.left.val))
                    result.append(node.left)
                else:
                    stack.append((node.left, max_val))
            if node.right: 
                if node.right.val >= max_val:
                    stack.append((node.right, node.right.val))
                    result.append(node.right)
                else:
                    stack.append((node.right, max_val))

        return len(result)

        