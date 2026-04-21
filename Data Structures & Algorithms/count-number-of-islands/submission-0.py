class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def islandExplore(r, c, grid, visted):
            if (r,c) in visited:
                return None
            elif min(r,c) < 0 or r == len(grid) or c == len(grid[0]):
                return None

            elif grid[r][c] == "0":
                return None
            
            else:
                visited.add((r,c))
                islandExplore(r-1, c, grid, visited)
                islandExplore(r+1, c, grid, visited)
                islandExplore(r, c-1, grid, visited)
                islandExplore(r, c+1, grid, visited)
                
                grid[r][c] = 0


        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                visited = set()
                if grid[i][j] == "1":
                    islandExplore(i, j, grid, visited)
                    counter += 1
        
        return counter

