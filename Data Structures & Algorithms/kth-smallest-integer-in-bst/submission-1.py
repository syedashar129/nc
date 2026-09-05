# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def dfs(node):
            # in order 
            nonlocal count 

            if not node:
                return None
            
            # left (return it up this is imp since we are looking at low val)
            left_res = dfs(node.left)
            if left_res is not None:
                return left_res

            # root
            count += 1
            if count == k:
                return node.val # found 
            
            # right 
            return dfs(node.right)
            
        
        return dfs(root)

    

