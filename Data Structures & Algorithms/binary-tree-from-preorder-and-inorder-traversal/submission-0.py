# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for k,v in enumerate(inorder):
            hashmap[v] = k
        preindex = 0
        def helper(l,r):
            nonlocal preindex
            if l>r:
                return None
            root_value = preorder[preindex]
            preindex += 1
            root = TreeNode(root_value)
            split_index = hashmap[root_value]
            root.left = helper(l,split_index-1)
            root.right = helper(split_index+1, r)

            return root
        return helper(0, len(inorder)-1)
            
        
