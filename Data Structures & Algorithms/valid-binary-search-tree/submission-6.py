# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(left, root, right):
            if root is None:
                return True
            elif not(left < root.val and root.val < right):
                return False
            else:
                checkLeft = isValid(left, root.left, root.val)
                checkRight = isValid(root.val, root.right, right)

                return checkLeft and checkRight

        return isValid(-1003, root, 1003)

