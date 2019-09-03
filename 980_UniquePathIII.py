class Solution:

    def __init__(self):
        self.num_paths = 0
        self.grid = []
        self.start_pos = (-1, -1)
        self.end_pos = (-1, -1)
        self.m = 0
        self.n = 0
    
    def dfs(self, t, x, y, res_empty):
            if 0<=x<self.m and 0<=y<self.n and t[x][y]:
                if res_empty == 1:
                    if abs(self.end_pos[0]-x)+abs(self.end_pos[1]-y)==1:
                        self.num_paths += 1
                    else:
                        return
                t[x][y] = False
                self.dfs(t, x-1, y, res_empty - 1)
                self.dfs(t, x+1, y, res_empty - 1)
                self.dfs(t, x, y-1, res_empty - 1)
                self.dfs(t, x, y+1, res_empty - 1)
                t[x][y] = True
                
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        num_empty = 0
        self.grid = grid
        t = [[True]*self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]==0:
                    num_empty += 1
                elif grid[i][j] == -1:
                    t[i][j] = False
                elif grid[i][j] == 1:
                    self.start_pos = (i, j)
                    t[i][j] = False
                else: #grid[i][j] = 2
                    self.end_pos = (i, j)
                    t[i][j] = False
        x, y = self.start_pos[0], self.start_pos[1]
        if num_empty:
            self.dfs(t, x-1, y,  num_empty)
            self.dfs(t, x+1, y,  num_empty)
            self.dfs(t, x, y-1,  num_empty)
            self.dfs(t, x, y+1,  num_empty)
        elif abs(self.end_pos[0]-x)+abs(self.end_pos[1]-y)==1: #WA一次 [1,2] 一开始没有想到没有empty 直接首尾相连的情况
            self.num_paths = 1
        return self.num_paths

        