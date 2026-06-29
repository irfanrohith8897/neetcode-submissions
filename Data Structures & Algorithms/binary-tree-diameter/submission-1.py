# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def height(root):
            nonlocal diameter
            if not root:
                return 0
            
            left=height(root.left)
            right=height(root.right)

            cur_diameter=left+right
            diameter=max(diameter,cur_diameter)

            return 1+max(left,right)
        height(root)
        
        return diameter
