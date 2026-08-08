class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x,y):
            if x >= n or y >= m or x < 0 or y < 0 or grid[x][y] != "1":
                return
            grid[x][y] = "0"
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1) 
        ni = 0
        n,m = len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ni += 1
                    dfs(i,j)
                else:
                    continue
        
        return ni