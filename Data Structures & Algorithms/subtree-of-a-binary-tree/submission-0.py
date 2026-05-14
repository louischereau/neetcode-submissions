# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isIdentical(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val != subRoot.val: return False
        if root and not subRoot or not root and subRoot: return False

        isLeftIdentical = self.isIdentical(root.left, subRoot.left)
        isRightIdentical = self.isIdentical(root.right, subRoot.right)

        return isLeftIdentical and isRightIdentical

        

    def isSubTreeCheck(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        isSubtree = self.isIdentical(root, subRoot)
        
        if isSubtree: return True

        isLeftSubtree = False
        isRightSubtree = False

        if root.left: isLeftSubtree = self.isSubTreeCheck(root.left, subRoot)
        if root.right: isRightSubtree = self.isSubTreeCheck(root.right, subRoot)
        
        return isLeftSubtree or isRightSubtree
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSubTreeCheck(root, subRoot)