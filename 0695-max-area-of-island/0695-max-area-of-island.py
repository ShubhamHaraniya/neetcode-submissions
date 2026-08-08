class Solution(object):
    def maxAreaOfIsland(self, grid):

        n = len(grid)
        m = len(grid[0])

        mx = 0
        curr = 0

        def dfs(x, y):
            nonlocal curr, mx

            if x >= n or y >= m or x < 0 or y < 0 or grid[x][y] != 1:
                mx = max(mx, curr)
                return

            curr += 1
            grid[x][y] = 0

            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    curr = 0
                    dfs(i, j)

        return mx