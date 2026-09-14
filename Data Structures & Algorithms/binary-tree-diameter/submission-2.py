# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, node):
        if node is None:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        self.best = max(self.best, left + right)
        return 1 + max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        self.depth(root)
        return self.best
