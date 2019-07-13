class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        """
        Do not return anything, modify board in-place instead.
        """
        def checkNeighbor(board, x, y):
            #一开始单独写了8个if 还是不够有统一性吖
            return 0<=x<len(board) and 0<=y<len(board[0]) and abs(board[x][y])==2

        debug =  False
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] += 1 
        #board = [[board[i][j]+1 for j in range(len(board[0]))] for i in range(len(board))] 这样不会被改变
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live_num = 0
                for k in range(8): #for I in range(-1:1): for J in range(-1:1)
                    live_num += checkNeighbor(board, i+dx[k],j+dy[k]) 
                if board[i][j] == 1 and live_num == 3:
                    board[i][j] *= -1
                if board[i][j] == 2 and (live_num < 2 or live_num > 3):
                        board[i][j] *= -1

        m = {2:1, 1:0, -2:0, -1:1}        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = m[board[i][j]]
        
        #board = [ [m[board[i][j]] for j in range(len(board[0]))] for i in range(len(board))]

        #对于infinite 如果无法把所有的存于内存 live的也属于稀疏矩阵 那么之前的方法就不太好 摘自@Stefan
        #不如把live的存好 emmm 但是emmm 其实这里还没有很看懂 需要继续消化吖
        def gameOfLifeInfinite(self, live):
            ctr = collections.Counter((I, J)
                    for i, j in live
                    for I in range(i-1, i+2)
                    for J in range(j-1, j+2)
                    if I!= i or J!=j)
            return {ij for ij in ctr
            if ctr[ij] == 3 or ctr[ij]==2 and ij in live}

        def gameOfLife(self, board):
            live = {(i,j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
            live = self.gameOfLifeInfinite(live)
            for i, row in enumerate(board):
                for j in range(len(row)):
                    row[j] = int((i,j) in live)
        