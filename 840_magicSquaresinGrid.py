class Solution(object):
    def check(self, grid, x, y):
        s = 0
        if grid[x][y] + grid[x+1][y+1] + grid[x+2][y+2] != 15 \
        or grid[x+2][y] + grid[x+1][y+1] + grid[x][y+2] != 15:
            return False
        for i in range(3):
            #WA1 in 直接s.union() 而么有 s = s.union()
            #s = s.union({grid[x+i][y], grid[x+i][y+1], grid[x+i][y+2]})
            #WA2 in 没有考虑1-9 所以如果0&10同时存在也会pass 那样的话 需要s == set((range(1,10))
            s += (1<<grid[x+i][y]) + (1<<grid[x+i][y+1]) + (1<<grid[x+i][y+2])
            if sum([grid[x+i][y], grid[x+i][y+1], grid[x+i][y+2]]) != 15 \
                or sum([grid[x][y+i], grid[x+1][y+i], grid[x+2][y+i]]) != 15:
                    return False
        return s == 1022
        
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)<3 or len(grid[0])<3:
            return 0
        cnt = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                cnt += self.check(grid,i,j)
        return cnt

    '''
    #中心必须=5 然后可以clock-wise是那些数
       def numMagicSquaresInside(self, g):
        def isMagic(i, j):
            s = "".join(str(g[i + x / 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return g[i][j] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)
        return sum(isMagic(i, j) for i in range(len(g) - 2) for j in range(len(g[0]) - 2) if g[i + 1][j + 1] == 5)
    '''
        