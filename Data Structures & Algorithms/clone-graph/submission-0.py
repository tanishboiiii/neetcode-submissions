"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            # if you have already visisted this node, then no need to create a clone
            # just return the cloned node 
            if node in oldToNew:
                return oldToNew[node]
            else:
                copy = Node(node.val)
                oldToNew[node] = copy

                for n in node.neighbors:
                    copy.neighbors.append(dfs(n))
                
                return copy

        if node:
            return dfs(node)
        else:
            return None