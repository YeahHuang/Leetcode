import collections, copy
#一个解 vs 多个解 
#是不是还是直接substr一下就好了哦

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_exist = False
        self.board = None
        self.word = ""
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.word = word
        cur.end = True

class Solution:
    #如果不用Trie 会TLE

    def __init__(self):
        self.ans = []
        self.trie = Trie()
        self.debug = True
        self.ori_board = None

    def findWords(self, board, words):
        
        for word in words:
            self.trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.traverseBoard( self.trie.root, board, i, j, "")
        return self.ans
        '''
        words.sort(key = lambda x: len(x), reverse = True)
        self.ori_board = board
        for word in words:
            flag_existed = False
            for existed_word in self.ans:
                if word in existed_word:
                    self.ans.append(word)
                    flag_existed = True
                    break
            if flag_existed == False and self.single_exist(board, word): #又一次compile error 因为 == 与 = 弄混淆 
                self.ans.append(word)
        return self.ans
        '''

    def traverseBoard(self, trie, board, x, y, cur_word):
        if trie.end:
            self.ans.append(cur_word)
            trie.end = False
        if (0<=x<len(board) and 0<=y<len(board[0])):      
            tmp = board[x][y]
            trie = trie.children.get(tmp)
            if trie:
                board[x][y] = "#"
                self.traverseBoard(trie, board, x+1, y, cur_word+tmp)
                self.traverseBoard(trie, board, x-1, y, cur_word+tmp)
                self.traverseBoard(trie, board, x, y+1, cur_word+tmp)
                self.traverseBoard(trie, board, x, y-1, cur_word+tmp)
                board[x][y] = tmp
        
    #最终解答只到这里为止 剩下的都是额外的失败探索

    def traverseTrie(self, trie, board, cur_word): #not worked too much space(each sol 1 board) needed for each word 
        if self.debug:
            print("In traverseTrie: ", cur_word, board, trie.end)
        if trie.end == True: #len(trie.children)==0
            if self.exist(board, cur_word)[1] or self.exist(self.ori_board, trie.word)[1]:
                self.ans.append(trie.word)
        elif len(trie.children)>1:
            after_board, is_exist =  self.exist(board, cur_word)
            if is_exist:
                if self.debug:
                    print("In traverse:", cur_word, "exists")
                for child in trie.children.keys():
                    self.traverseTrie(trie.children[child], after_board, child)
        else:
            for child, next_trie in trie.children.items():#其实不用for 因为只有一个 我只是不知道如何调用了而已 
                self.traverseTrie(trie.children[child], board, cur_word + child) 
    
    def single_exist(self, board, word: str) -> bool: #original exist
        global is_exist, dx,dy,m,n
        is_exist = False
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        def dfs(step, x, y, board):
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

        m, n = len(board),len(board[0])
        for i, line in enumerate(board):
            for j, char in enumerate(line):
                if char == word[0]:
                    board[i][j] = '#'
                    dfs(1, i, j, board)
                    board[i][j] = word[0]
                    if is_exist:    #如果最好只有一个出口 可优化为break
                        return True
        return is_exist
 
    
    def exist(self, board, word: str):
        global dx,dy,m,n #新巩固了python的global使用
        #global is_exist
        #is_exist = False 
        if self.debug:
            print("In exist", word, board)
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        def dfs(step, x, y, board): #其实如果+ret 就可以不用global is_exist 了 可以自己衡量一下
            global is_exist, dx,dy, m, n
            if step == len(word):
                is_exist = True
                return (board, -1, -1, True)
            #if is_exist:
            #    return 
            for i in range(4):
                tx, ty = x+dx[i], y+dy[i]
                if  0<=tx<m and 0<=ty<n and board[tx][ty]==word[step]:
                    board[tx][ty] = '#'
                    after_board, last_x, last_y, is_exist = dfs(step+1, tx, ty, board)
                    if is_exist:
                        if last_x == -1 and last_y == -1:
                            last_x, last_y = tx, ty 
                        return (after_board, last_x, last_y, True)
                    board[tx][ty] = word[step]
            return (None, False)
            
        m, n = len(board),len(board[0])
        if word=="":
            return (board, True)
        for i, line in enumerate(board):
            for j, char in enumerate(line):
                if char == word[0]:
                    board[i][j] = '#'
                    after_board, is_exist = dfs(1, i, j, board) 
                    board[i][j] = word[0] 
                    if is_exist:    #如果最好只有一个出口 可优化为break
                        return (after_board, True)
                    
        return (None, False)
    
'''
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = []
'''
board = [["a","b"],["c","d"]]
words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
sol = Solution()
print(sol.findWords(board, words))