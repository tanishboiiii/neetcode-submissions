# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balance = True

        def height(root):
            nonlocal is_balance

            if root is None:
                return 0
            else:
                left = height(root.left)
                right = height(root.right)

                if abs(left - right) > 1:
                    is_balance = False  
                
                return 1+max(left, right)

        height(root)
        return is_balance