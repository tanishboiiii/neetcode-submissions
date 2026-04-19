# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        Q = [root]

        while len(Q) > 0:
            qLen = len(Q)
            rightMost = Q[-1]
            
            if rightMost is not None:
                res.append(rightMost.val)
            
            for i in range(qLen):
                curr = Q.pop(0)
                if curr:
                    if curr.left:
                        Q.append(curr.left)
                    if curr.right:
                        Q.append(curr.right)
            
        return res
