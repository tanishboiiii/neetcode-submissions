class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def islandExplore(r, c, grid):
            if min(r,c) < 0 or r == len(grid) or c == len(grid[0]):
                return None

            elif grid[r][c] == "0":
                return None
            else:
                grid[r][c] = "0" 
                islandExplore(r-1, c, grid)
                islandExplore(r+1, c, grid)
                islandExplore(r, c-1, grid)
                islandExplore(r, c+1, grid)
                


        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islandExplore(i, j, grid)
                    counter += 1
        
        return counter

