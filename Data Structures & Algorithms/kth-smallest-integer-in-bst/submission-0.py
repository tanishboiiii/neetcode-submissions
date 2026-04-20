# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elem = []
        def inorder(root):
            if root is None:
                return None
            else:
                inorder(root.left)
                elem.append(root.val)
                inorder(root.right)

        inorder(root)
        return elem[k-1]
            