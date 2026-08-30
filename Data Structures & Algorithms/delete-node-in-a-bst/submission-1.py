# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Search 
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # node found
            # case 1 and case 2
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            
            # case 3 -- find smallest in right side
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val # replace the successor
            root.right = self.deleteNode(root.right, root.val) # delete the successor from righ 
        
        return root # for recurivse ignoring

