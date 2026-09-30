# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        res = 0

        def dfs(root, res) -> int:
            if not root:
                return 0
            x = 0
            if high >= root.val >= low:
                x += root.val
            left = dfs(root.left, res)
            right = dfs(root.right, res)
            return x + left + right

        res = dfs(root, res)

        return res
