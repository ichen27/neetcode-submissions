# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterate through tree
        # Left val and right val swap
        # Use a temp variable
        # Check if node is valid and if children are valid
        # if node not valid, return
        # if a child not valid, swap with empty
        

        def recursive_helper(node):
            if node is None:
                return

            temp = node.left
            node.left = node.right
            node.right = temp

            recursive_helper(node.left)
            recursive_helper(node.right)


        recursive_helper(root)

        return root
        