class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        flag = True # 最大的问题是你不应该一个一个判断 而是最终生成了终结的代码
        p1 = len(S) - 1
        p2 = len(T) - 1
        while p1>=0 or p2>=0:
            if p1>=0 and S[p1]=='#':
                temp = p1
                while p1>=0 and S[p1]=='#':
                    p1 -= 1
                p1 -= (temp-p1)
                if p1<0:
                    p1 = -1
            if p2>=0 and T[p2]=='#':
                temp = p2
                while p2>=0 and T[p2]=='#':
                    p2 -= 1
                p2 -= (temp-p2)
                if p2<0:
                    p2 = -1
            print(p1,p2)
            if p1>=0 and p2>=0:
                if S[p1]==T[p2]:
                    p1 -=1
                    p2 -=1
                else:
                    flag = False
                    break
            elif p1 < 0 and p2 < 0:
                break
            '''
            else:
                flag = False
                break
            
            #WA 了 3次  
            e.g. 还是没考虑全面吖 "bxj##tw"
            "bxo#j##tw"
            '''
        return flag
 
class Solution(object): #AC了 但又丑又长
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S_after = ""
        lenS = 0
        T_after = ""
        lenT = 0
        for c in S:
            if c=='#':
                if lenS:
                    lenS -= 1
            else:
                S_after = S_after[0:lenS]
                S_after += c
                lenS += 1
        for c in T:
            if c=='#':
                if lenT:
                    lenT -= 1
            else:
                T_after = T_after[0:lenT] #一开始WA的是因为这里写成了 T_after = T_after[0:lenS]
                # 我发现我经常有这种复制粘贴 直接改 少给了一两个的bug 最好是能写成func 或者统一用自带的修改
                T_after += c
                lenT += 1
        print(S_after, lenS)
        print(T_after, lenT)
        S_after = S_after[0:lenS]
        T_after = T_after[0:lenT]
        return S_after==T_after   

#下面部分不是我原创的 是看了官方solution的～
class Solution(object): #看看人家的 def build 这代码多优雅 
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans: 
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)

class Solution(object): 
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S): #reversed竟然不用占空间哦
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x        #关于yield https://blog.csdn.net/mieleizhi0522/article/details/82142856
        return all(x == y for x, y in itertools.izip_longest(F(S),F(T)) #这儿的函数一个不懂 要好好学下了
