# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def search(self, root, target):
        if root is None:
            return False
        elif root.val == target:
            return True
        elif target < root.val:
            return self.search(root.left, target)
        else:
            return self.search(root.right, target)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        low = min(p.val, q.val)
        high = max(p.val, q.val)

        ans = root   # store the node, not root.val

        def dfs(root, p, q):
            nonlocal ans

            if root is None:
                return

            if low <= root.val <= high:
                p_found = self.search(root, p.val)
                q_found = self.search(root, q.val)

                if p_found and q_found:
                    if root.val < ans.val:
                        ans = root

            dfs(root.left, p, q)
            dfs(root.right, p, q)

        dfs(root, p, q)
        return ans