class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        queue = []
        visit = set()

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROW or c == COL or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            queue.append([r, c])

        # now you have all your source nodes, start your traversal
        # bfs style from them

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visit.add((r,c))


        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.pop(0)
                grid[r][c] = dist
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1


        

                