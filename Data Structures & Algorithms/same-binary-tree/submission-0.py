# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = [p]
        queue_q = [q]

        while len(queue_p) > 0 or len(queue_q) > 0:
            node_p = queue_p.pop(0)
            node_q = queue_q.pop(0)

            if not node_p and node_q or node_p and not node_q:
                return False

            if not node_p and not node_q:
                continue

            if node_p.val != node_q.val:
                return False

            if node_p.left:
                queue_p.append(node_p.left)
            else:
                queue_p.append(None)

            if node_q.left:
                queue_q.append(node_q.left)
            else:
                queue_q.append(None)


            if node_p.right:
                queue_p.append(node_p.right)
            else:
                queue_p.append(None)

            if node_q.right:
                queue_q.append(node_q.right)
            else:
                queue_q.append(None)

        return True



        