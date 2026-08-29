# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. both null so reached end of both
        if not p and not q: 
            return True 
        
        # 2. only one node or node val diff
        if not p or not q or p.val != q.val:
            return False

        # 3. Both current nodes match --> check childerenn
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

