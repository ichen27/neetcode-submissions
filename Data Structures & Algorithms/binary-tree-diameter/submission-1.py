# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive function
        # Add one on each iteration, take max
        # Diameter is Height of Left Tree + Right Tree
        
        diameter = 0

        def dfs_helper(node):
            # Finds height of node
            nonlocal diameter

            if node == None:
                return 0

            left = dfs_helper(node.left)
            right = dfs_helper(node.right)
            diameter = max(diameter, left + right)

            return 1 + max(dfs_helper(node.left), dfs_helper(node.right))

        dfs_helper(root)
        return diameter


        

        
