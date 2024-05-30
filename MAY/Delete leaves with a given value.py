# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left is None and root.right is None and root.val==target:
            return None
        def dfs(root):
            if not root:
                return True
            if root.val==target and not root.left and not root.right:
                return True
            if root:
                left=False
                if not root.left:
                    left=True
                right=False
                if not root.right:
                    right=True
                if root.left and dfs(root.left) and root.left.val==target:
                    root.left=None
                    left=True
                if root.right and dfs(root.right) and root.right.val==target:
                    root.right=None
                    right=True
                return left and right
            return False

        dfs(root)
        if root and not root.left and not root.right and root.val==target:
            return None
        return root
    