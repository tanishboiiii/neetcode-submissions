class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        for dest, src in prerequisites:
            if src not in adjList:
                adjList[src] = []

            if dest not in adjList:
                adjList[dest] = []

            adjList[src].append(dest) 

        def dfs(crs, adjList, path, visit):
            if crs in path:
                return False
            elif crs in visit: # already seen before don't want to redo work, but not a 
                return True      # not a cycle though...
            else:
                visit.add(crs)
                path.add(crs)

                for i in adjList[crs]:
                    if not dfs(i, adjList, path, visit):
                        return False

                path.remove(crs)
                return True

        visit = set()

        for course in adjList:
            path = set()
            if not dfs(course, adjList, path, visit):
                return False
        
        return True