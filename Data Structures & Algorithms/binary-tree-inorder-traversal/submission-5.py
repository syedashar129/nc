# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return # res is already []
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return res


        



# we can use bfs or dfs here
# we will use recursive dfs here
# time complexity: O(n)
# space: O(n)