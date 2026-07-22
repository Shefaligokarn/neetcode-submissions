# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0
        def helper(root):
            nonlocal dia
            
            if not root:
                return 0
            l_h = helper(root.left)
            r_h = helper(root.right)
            dia = max(dia, l_h+r_h)
            return 1 + max(l_h, + r_h)
        helper(root)
        return dia