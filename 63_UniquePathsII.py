class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        t = [[1-obstacleGrid[i][j] for j in range(n)] for i in range(m)]
        for j in range(1,n): #WA一次 因为一开始没有加这两段预判断 忽略了第一行&第一列的通路情况
            if t[0][j-1]==0:
                t[0][j] = 0
        for i in range(1,m):
            if t[i-1][0] == 0:
                t[i][0] = 0
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    t[i][j] = t[i-1][j]+t[i][j-1]
        return t[m-1][n-1]