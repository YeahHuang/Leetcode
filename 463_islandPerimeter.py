class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def judgeWater(x: int, y: int) -> int:
            return not(0<=x<m and 0<=y<n and grid[x][y]==1)

        if grid == [[]]:
            return 0
        qpp, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):  
                if grid[i][j]: #一开始这一行忘记加了
                    qpp += judgeWater(i-1,j) + judgeWater(i+1,j) + judgeWater(i,j-1) + judgeWater(i,j+1)
        return qpp