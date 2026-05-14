# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Use a list as a queue for BFS traversal
        queue = [(p, q)]

        # The loop runs as long as there are pairs of nodes to compare
        while queue:
            node_p, node_q = queue.pop(0)

            # 1. Check if both are None (Base Case: End of branch, they match)
            if not node_p and not node_q:
                continue

            # 2. Check if one is None and the other is not (Structure/Size Mismatch)
            # This covers the case 'if not node_p and node_q or node_p and not node_q'
            if not node_p or not node_q:
                return False

            # 3. Check if values are different
            if node_p.val != node_q.val:
                return False

            # 4. If all checks pass, enqueue the children pairs for the next level
            # We don't need to append 'None' placeholders; the checks above handle the structural mismatch.
            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))

        return True



        