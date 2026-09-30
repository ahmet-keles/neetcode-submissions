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
        x = 0
        if high >= root.val >= low:
            x = root.val
        left = 0
        right = 0
        if root.val > low:
            left = self.rangeSumBST(root.left, low, high)
        if root.val < high:
            right = self.rangeSumBST(root.right, low, high)

        return x + left + right
