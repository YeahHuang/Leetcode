class Solution:
    def confusingNumberII(self, n: int) -> int:
        '''
        6,9 肯定都是了  纸质草稿一定也要有
        2位： 2 + （C21 * C41 * 2 + 2） + C21 * C21  = 2+ 18+4 = 24
        3位： 2 + (A22 * C32 * C41 + C21 * C32 * C41) + C21 * C31 * C31 * C31 + 
        '''
        
        def checkValid(s):
            if len(s)&1 and s[len(s)//2] in {'6','9'}:
                return True
            equals_reverse = True
            for i in range(len(s)//2):
                if (s[i] == '6' and s[-i-1] != '9') \
                or (s[i] == '9' and s[-i-1] != '6') \
                or (s[i] in {'0','1','8'} and s[i] != s[-i-1]): #WA1 写成了{0,1,8}
                    equals_reverse = False
                    break
            return equals_reverse == False
        
        global cnt
        
        def dfs(idx, max_len, cur_s, s): #一开始没想dfs 想直接死算 就不太好
            global cnt
            if cur_s > s:
                return
            if idx == max_len:
                '''
                #一开始没有写checkValid函数 就很冗长 代码不好看
                cur_s = list(cur_s)
                for i in range((len(cur_s)+1)//2):
                    if cur_s[i]=='6':
                        cur_s[i] = '9'
                    elif cur_s[i]=='9':
                        cur_s[i] = '6'
                '''
                
                if checkValid(cur_s):
                    print(cur_s)
                    cnt += 1
                return
            if idx!=0:
                dfs(idx+1, max_len, cur_s + '0', s)
            for c in ['1','6','8','9']:
                dfs(idx+1, max_len, cur_s+c, s)
        
        '''
        cnt = 0
        for i in range(101):
            if checkValid(str(i)):
                print(i)
                cnt += 1
        print("cnt",cnt)'''
        
        
        
        f = [0, 2, 16, 88, 480, 2440, 12400, 62200, 312000, 1561000]
        if 10**(len(str(n))-1) == n:
            return sum(f[:len(str(n))]) + 1
        cnt = sum(f[:len(str(n))])
         
        dfs(0, len(str(n)),"",str(n))
        return cnt
        
        #2位： 4*5 - 4 = 16
        #3位： 4*5*5 - 4*3 = 100 - 12 = 88
        #4位： 4*5*5*5 - 4*5 = 500 - 20 = 480
        #5位： 4*5*5*5*5 - 4*5*3 = 2500 - 60 = 2440
        #6位： 4*5*5*5*5*5 - 4*5*5 = 12500 - 100 = 12400
        #7位： 4*5*5*5*5*5*5 - 4*5*5*3 = 62500 - 300 = 62200
        #8位： 4*5*5*5*5*5*5*5 - 4*5*5*5 = 312000
        #9位： 4*5*5*5*5*5*5*5*5 - 4*5*5*5*3 = 1561000

         