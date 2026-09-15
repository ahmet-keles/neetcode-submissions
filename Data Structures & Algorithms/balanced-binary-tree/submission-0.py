# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root) -> int:
        if root is None:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)

        if abs(left - right) > 1:
            self.balance = False
        
        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        self.depth(root)
        return self.balance
        
        