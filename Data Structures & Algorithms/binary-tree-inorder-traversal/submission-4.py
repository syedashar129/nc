# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        left_values = self.inorderTraversal(root.left)
        right_values = self.inorderTraversal(root.right)

        return [*left_values, root.val, *right_values]


        



# we can use bfs or dfs here
# we will use recursive dfs here
# time complexity: O(n)
# space: O(n)