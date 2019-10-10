class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dx = [-1,0,1,0]
        dy = [0,1,0,-1] 
        ''' 顺时针旋转90度 可以直接用  dx, dy = dy, -dx
        逆时针则可以直接用 dx, dy = -dy, dx
        '''
        dir, x, y = 0, 0, 0
        went = set([(0,0)])
        maxi = 0
        for i in range(4):
            for ins in instructions:
                if ins=='G':
                    x, y = x+dx[dir], y+dy[dir]
                    maxi = max(maxi, x**2 + y**2)
                    went.add((x,y))
                elif ins == 'L':
                    dir = (dir-1)%4
                else:
                    dir = (dir+1)%4
        for i in range(4):
            for ins in instructions:
                if ins=='G':
                    x, y = x+dx[dir], y+dy[dir]
                    if x**2 + y**2 > maxi:
                        return False
                elif ins == 'L':
                    dir = (dir-1)%4
                else:
                    dir = (dir+1)%4
        return True

    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R': dx, dy = dy, -dx
            if i == 'L': dx, dy = -dy, dx
            if i == 'G': x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0,1)