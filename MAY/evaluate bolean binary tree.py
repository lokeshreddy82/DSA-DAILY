# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def checker(value):
            return value==1
        def dfs(root):
            if root and not root.left and not root.right:
                return bool(root.val)
            return dfs(root.left) | dfs(root.right) if root.val==2 else dfs(root.left)& dfs(root.right)
        return dfs(root)