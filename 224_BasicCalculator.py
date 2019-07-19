class Solution:
    def calculate(self, s: str) -> int:
        #TLE
        def new_calculate(s:str) -> int:
            operator_list, num_list = ['(','+'], []
            n, ans, i, debug = len(s), 0, 0, True
            while i<n:
                if s[i].isdigit():
                    start_idx = i
                    while i<n and s[i].isdigit()
                        i += 1
                    num_list.append(int(s[start_idx:i]))
                    i-=1
                elif s[i] == '(':
                    operator_list = operator_list + ['(','+']
                elif s[i] == '+' or s[i]=='-':
                    operator_list.append(s[i])
                elif s[i] == ')':
                    qpp = 0
                    while True:
                        op = operator_list.pop()
                        if op == '+':   
                            qpp += num_list.pop()
                        elif op == '-':
                            qpp -= num_list.pop()
                        elif op == '(':
                            break
                        else:
                            print("ERROR! op not in + - (", op)
                    num_list.append(qpp)
                    if debug: print("qpp = %d"%(qpp))
                else:
                    print("ERROR! i=%d s[i]=%s"%(i,s[i]))
                i+=1

        def dashen_calculate(s:str) -> int:
            ans,i,n = 0,0,len(s)
            operator_list = [1,1] #表示被省略的+ 和 加上[-1]判断（前的符号的时候可以有个1
            while i<n:
                if s[i].isdigit():
                    start_idx = i
                    while i<n and s[i].isdigit():
                        i += 1
                    ans += operator_list.pop() * int(s[start_idx:i])
                elif s[i] in '+=(':
                    operator_list += signs[-1] * (1, -1)[s[i]=='-'] #这个用法真的很酷吖 相当于true 就是 1 就是 -1
                    i+=1
                elif s[i] == ')':
                    operator_list.pop()
            return ans

        def dfs_calculate(s: str) -> int:
            operator_list = ['+']
            num_list = []
            n = len(s)
            ans = 0
            i = 0
            debug = False
            if debug:
                print("is going to calculate ",s)
            while i<n:
                if debug:   print("s[%d]=%s"%(i,s[i]))
                if '0'<=s[i]<='9':
                    start_idx = i
                    while i<n and '0'<=s[i]<='9':
                        i += 1
                    num_list.append(int(s[start_idx:i]))
                    if operator_list[-1]=='+':
                        ans += num_list[-1]
                    else:
                        ans -= num_list[-1]
                    if debug:
                        print("Is digit from %d to %d  %d, now ans = %d"%(start_idx, i, num_list[-1], ans))
                elif s[i]=='(':
                    start_idx = i+1
                    i += 1
                    paren_num = 1
                    while i<n:
                        if s[i]=='(':   paren_num += 1
                        if s[i]==')': 
                            paren_num -= 1
                            if paren_num == 0:
                                if debug:
                                    print("Is going to calculate from %d to %d"%(start_idx, i))
                                num_list.append(dfs_calculate(s[start_idx:i]))
                                if operator_list[-1]=='+':
                                    ans += num_list[-1]
                                else:
                                    ans -= num_list[-1]
                                i+=1
                                break
                        i+=1
                elif s[i]=='+' or s[i]=='-':
                    operator_list.append(s[i])
                    if debug:
                        print(operator_list)
                    i+=1
                else:
                    print("ERROR! i=%d s[i]=%s"%(i,s[i]))
                    i+=1
            return ans
        return new_calculate(s.replace(' ',''))