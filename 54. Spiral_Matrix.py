class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #1次AK 8ms 
        if len(matrix)==0:  return []
        m, n = len(matrix), len(matrix[0])
        not_visited = [[True for j in range(n)]for i in range(m)]
        spiral_list = []
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        cur_dir = 0
        x = 0
        y = 0
        while True:
            while 0<=x<m and 0<=y<n and not_visited[x][y]:
                spiral_list.append(matrix[x][y])
                not_visited[x][y] = False
                x += dx[cur_dir]
                y += dy[cur_dir]
            x -= dx[cur_dir]
            y -= dy[cur_dir]
            cur_dir = (cur_dir + 1) % 4
            x += dx[cur_dir]
            y += dy[cur_dir]
            #一开始忘记写了0<=x<m and 0<=y<n的判断 被自己的[[1]]的case测出来了
            #以后用了数组 为了避免 out of bound 的 exception 就先写上界限判断吧
            if not (0<=x<m and 0<=y<n and not_visited[x][y]): 
                break

        return spiral_list

        '''
        [[]]
        [[1]]
        [[1,2,3,4]]
        [[1],[2],[3]]
        [[1,2],[3,4]]
        '''