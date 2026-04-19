# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0

        def dfs(root, maxVal):
            nonlocal counter

            if root is None:
                return 
            else:
                maxVal = max(root.val, maxVal)
                if root.val >= maxVal:
                    counter += 1
                
                dfs(root.left, maxVal)
                dfs(root.right, maxVal)

                return root.val

        dfs(root, root.val)
        return counter