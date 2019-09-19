class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(x, y, board,  row,  col, squa) -> bool:
            if y==9:
                if x == 8:
                    return True
                else:
                    x, y = x+1, 0 
            while (board[x][y]!='.'):    
                y+=1       
                if y==9:
                    if x == 8:
                        return True
                    else:
                        x, y = x+1, 0
            avail = row[x] & col[y] & squa[x//3*3 + y//3]
            for num in avail:
                board[x][y] = num
                #print(num, row[x], col[y],squa[x//3*3 + y//3])
                row[x].remove(num)
                col[y].remove(num)
                squa[x//3*3 + y//3].remove(num)
                if dfs(x, y+1, board, row, col, squa):
                    return True
                row[x].add(num)
                col[y].add(num)
                squa[x//3*3 + y//3].add(num)
                board[x][y] = '.'  #WA 一次 一开始忘记复原了
            return False
        """
        Do not return anything, modify board in-place instead.
        """
        
        row, col, squa = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for i in range(9):
            row.append(set())
            col.append(set())
            squa.append(set())
            for j in range(1,10):
                row[i].add(str(j))
                col[i].add(str(j))
                squa[i].add(str(j))

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    row[i].remove(board[i][j])
                    col[j].remove(board[i][j])
                    squa[i//3*3 + j//3].remove(board[i][j])
               
        dfs(0, 0, board, row, col, squa)
 
       