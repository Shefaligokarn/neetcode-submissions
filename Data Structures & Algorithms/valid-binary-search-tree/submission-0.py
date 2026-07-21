# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lowest = float("-inf")
        highest = float("inf")
        
        def helper(root, lowest, highest):
            if not root:
                return True
            if not (lowest < root.val < highest):
                return False
            return (helper(root.left, lowest, root.val) and helper(root.right,root.val,highest))



        return helper(root,lowest,highest)
            