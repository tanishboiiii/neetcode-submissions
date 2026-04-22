class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def islandArea(r: int, c: int, grid:List[List[int]]) -> int:
            area = 1
            queue = []
            queue.append([r,c])
            grid[r][c] = 0
            
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while queue:
                for i in queue:
                    row, col = queue.pop(0)
                    
                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc
                        if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or grid[nr][nc] == 0:
                            continue

                        queue.append((nr, nc))
                        grid[nr][nc] = 0    
                        area += 1
            
            return area
        
        maxArea = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, islandArea(i, j, grid))

        return maxArea