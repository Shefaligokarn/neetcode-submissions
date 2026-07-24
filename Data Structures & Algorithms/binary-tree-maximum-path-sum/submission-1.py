# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def helper(node):
            nonlocal max_sum
            
            if not node:
                return 0

            left_gain = max(0, helper(node.left))
            right_gain = max(0, helper(node.right))

            max_sum = max(max_sum, node.val+left_gain+right_gain)


            return node.val + max(right_gain,left_gain)

        helper(root)
        return max_sum

            