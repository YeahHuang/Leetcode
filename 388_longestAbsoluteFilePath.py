class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def cntTab(s:str): #可以直接line.count('\t') 或者 ine.lstrip('\t') 
            i, cnt, n = 0, 0, len(s)
            while i<n-1:
                if s[i:i+4]=='    ':
                    cnt+=1
                    i+=4
                else:
                    break
            return cnt
        
        input = input.replace("\t","    ") #WA1 \t 4*space的替换 一定要这个方向才最稳妥
        lines = input.split('\n') #可以改为input.splitlines()
        stack = [(0, -1)] #(length, depth)
        ans = 0 
        debug = True
        for line in lines:
            cnt = cntTab(line)
            if True:
                if '.' in line:
                    while cnt < stack[-1][1] + 1: #WA2 一开始这里忘记写了 只记得写下面的
                        stack.pop()
                    ans = max(ans, stack[-1][0]+len(line)-(stack[-1][1]+1)*4)
                else:
                    while cnt < stack[-1][1] + 1:
                        stack.pop()
                    if cnt != stack[-1][1] + 1:
                        print("ERROR! depth not consistent")
                    stack.append((stack[-1][0]+len(line)-(stack[-1][1]+1)*4+1, cnt))
                    if debug:
                        print("After: ", stack)
        return ans

'''
python的strip strip去除首/尾的 \n、\r、\t、' ')
>>> str = ' ab cd '
>>> str
' ab cd '
>>> str.strip() #删除头尾空格
'ab cd'
>>> str.lstrip() #删除开头空格
'ab cd '
>>> str.rstrip() #删除结尾空格
' ab cd'

>>> str2 = '1a2b12c21'
>>> str2.strip('12') #删除头尾的1和2
'a2b12c'
>>> str2.lstrip('12') #删除开头的1和2
'a2b12c21'
>>> str2.rstrip('12') #删除结尾的1和2
'1a2b12c'      
'''