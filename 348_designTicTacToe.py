class TicTacToe:


    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n 
        self.hor = [[0]*n for _ in range(2)] #其实这里可以不用设置2个， 只要 +1 / -1 然后绝对值=self.n 即可
        self.ver = [[0]*n for _ in range(2)]
        self.dia = [[0]*2 for _ in range(2)]
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        winner = 0 
        self.hor[player-1][row] += 1 
        self.ver[player-1][col] += 1
        if self.hor[player-1][row] == self.n or self.ver[player-1][col]  == self.n: #WA一次 因为后一个判断 写成了self.ver[player-1][row] 
            winner = player
        if row==col or row+col+1==self.n:
            self.dia[player-1][row==col] += 1
            if self.dia[player-1][row==col] == self.n: #Compile Error 一次 因为判断句 = 与 == 没写清楚 
                winner = player
            if row==col and row+col+1 == self.n: #WA一次 一开始center位 +2 的情况没考虑进去 
                self.dia[player-1][0] += 1
                if self.dia[player-1][0] == self.n:
                    winner = player
        #更清晰的版本： if self.n(另一句替换为 if -self.n in ...) in [self.hor[row], self.ver[col]. self.diag, self.anti_diag]  
        return winner

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)