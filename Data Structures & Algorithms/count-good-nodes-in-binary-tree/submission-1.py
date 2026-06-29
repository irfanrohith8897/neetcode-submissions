# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal=float('-inf')
        res=0
        def solve(node,maxVal):
            if not node:
                return 
            nonlocal res
            if node.val>=maxVal:
                res+=1
                maxVal=node.val
            solve(node.left,maxVal)
            solve(node.right,maxVal)

        solve(root,maxVal)
        return res
            