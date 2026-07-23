# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None
        def helper(root):
            nonlocal count, result
            if not root or result is not None: 
                return
            
            helper(root.left)
            count += 1
            if count ==k:
                result = root.val
                return
            helper(root.right)
            
        
        helper(root)
        return result