# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maximum):
            if not root:
              return 0
            if root.val >= maximum:
              count = 1
            else:
              count =0
              
            maximum = max(root.val, maximum)
            return (count + helper(root.left,maximum)+ helper(root.right,maximum))
        return helper(root,float("-inf"))