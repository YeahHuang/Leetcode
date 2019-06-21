class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Sol 1 mine      68ms
        def check(nine: List[str]) -> bool:
            flag = [False for i in range(10)]
            ret = True
            for s in nine:
                if s!='.':
                    if not flag[int(s)]:
                        flag[int(s)] = True
                    else:
                        ret = False
                        break
            return ret

        isValidSudoku = True
        for i in range(9):
            tmp_col = [board[j][i] for j in range(9)]
            tmp_square = [board[i//3*3 + j//3][i%3*3 + j%3]  for j in range(9)]
            if not check(board[i]) or not check(tmp_col) or not check(tmp_square):
                isValidSudoku = False
                break

        return isValidSudoku

        #Sol2 check的优化 52ms

        def check(nine: List[str]) -> bool: #看看别人写的set碾压的力量！
            nine = [i for i in nine if i != '.']
            return len(set(nine)) == len(unit)

        #Sol3 用enumerate 真优雅 真好看！   40ms              
        seen = [x for i, row in enumerate(board)
                    for j, c in enumerate(row)
                        if c!='.'
                            for x in ((c,i), (j,c), (i//3, j//3, c))]
        return len(seen) == len(set(seen))