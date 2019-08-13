import copy
class Record:
    def __init__(self, x, y, step, visited):
        self.x = x
        self.y = y
        self.step = step
        self.visited = visited

class Solution:
    #Sol1 BFS 因为deepcopy太耗时 会TLE
    def exist(self, board, word: str) -> bool:
        def equals(x,y,target):
            '''
            if x==0 and y==1:
                print(x,y,m,n,target,board[x][y],visited[x][y])
                print(False==False)
                print((not False))
                b = visited[x][y]
                print(visited[x][y])
                print((not b))
                print((not (visited[x][y])))
            '''
            return 0<=x<m and 0<=y<n and board[x][y]==target and visited[x][y]==False

        l = r = 0
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        pos = {}
        is_exist = True
        debug = False
        #预处理生成pos 记录位置信息
        for c in word:
            if c not in pos:
                pos[c] = []
                for i, line in enumerate(board):
                    for j, char in enumerate(line):
                        if char==c:
                            pos[c].append((i,j))
                if len(pos)==0:
                    is_exist = False
                    break
        if debug:
            print(pos)

        if is_exist:
            records = []
            is_exist = False
            m, n = len(board),len(board[0])
            #no_visited = [['False']*n for _ in range(m)] 不行了 年度top10 最蠢bug
            no_visited = [[False]*n for _ in range(m)]
            for x,y in pos[word[0]]:
                #tmp = no_visited.copy()
                tmp = copy.deepcopy(no_visited)
                if debug:
                    print(tmp)
                    print(no_visited)
                tmp[x][y] = True
                if debug:
                    print(tmp)
                records.append(Record(x,y,0, tmp))
            while records:
                record = records.pop(0)
                x, y, step, visited = record.x, record.y, record.step, record.visited
                if debug:
                    print(x,y, step)
                    print(visited)
                if step < len(word)-1:
                    target = word[step+1]
                    for i in range(4):
                        if equals(x+dx[i],y+dy[i],target):
                            if debug:
                                print(x+dx[i],y+dy[i],target)
                            tmp = copy.deepcopy(visited)
                            tmp[x+dx[i]][y+dy[i]] = True
                            records.append(Record(x+dx[i],y+dy[i],step+1, tmp))
                else:
                    is_exist = True
                    break
        return is_exist

    #Sol2 DFS
    def exist(self, board, word: str) -> bool:
        global is_exist, dx,dy,m,n #新巩固了python的global使用
        is_exist = False 
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        def dfs(step, x, y, board): #其实如果+ret 就可以不用global is_exist 了 可以自己衡量一下
            global is_exist, dx,dy, m, n
            if step == len(word):
                is_exist = True
                return
            if is_exist:
                return
            for i in range(4):
                tx, ty = x+dx[i], y+dy[i]
                if  0<=tx<m and 0<=ty<n and board[tx][ty]==word[step]:
                    board[tx][ty] = '#'
                    dfs(step+1, tx, ty, board)
                    board[tx][ty] = word[step]
            '''
            去除global的dx dy 但同样简洁美观的check方式
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
                return False
            res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
            '''
        m, n = len(board),len(board[0])
        for i, line in enumerate(board):
            for j, char in enumerate(line):
                if char == word[0]:
                    board[i][j] = '#'
                    dfs(1, i, j, board)
                    if is_exist:    #如果最好只有一个出口 可优化为break
                        return True
                    board[i][j] = word[0]
        return is_exist


board = [["A","A"],["C","E"]]
words = ["AA"]
sol = Solution()
for word in words:
    print(sol.exist(board,word))