class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = -1 #一开始因为 0-False 其他-数本身 WA了一次 因为会忽略num=0的情况
        self.num = -1

class Trie:
    def __init__(self,max_depth):
        self.root = TrieNode() 
        #self.max_depth = max_depth
        #self.max_match = 0 
        #self.perfect_match = False
        self.max_xor = 0

    def insert(self, num, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.end = num

    def search(self, num, word):
        cur = self.root
        for i,c in enumerate(word):
            if cur.children.get(c) is None:
                cur = cur.children[str(1-int(c))]
            else:
                cur = cur.children[c]
        self.max_xor = max(self.max_xor, num ^ cur.end)
    '''
    #把接下来的2坨 换成⬆️ 可以1184ms -> 1012ms 优化了查找 直接去match
    def search(self, num, word):
        cur = self.root
        for i,c in enumerate(word):
            if cur.children.get(c) is None:
                match_idx = i
                break
            else:
                cur = cur.children.get(c) 

        if i>=self.max_match:
            self.max_match = i
            if i == self.max_depth:
                self.perfect_match = True
                self.max_xor = cur.end ^ num
            else:
                self.calculate(num, cur)

    def calculate(self, num:int, cur:TrieNode)->None:
        if cur.end>0:
            self.max_xor = max(self.max_xor, num^cur.end)
        else:
            for c in cur.children.keys():
                self.calculate(num, cur.children.get(c))
    '''


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        '''
        每一个数push进对应的32的list 每到空的那一位 把所有的int push进一个list
        一个个的对照 去看 哪一个被miss 
        每一个在分析完后可以立刻得到自己的miss point list？
       
        O 
        '''
        
        #Sol3.0 Trie的优化 1012ms
        debug = True
        maxi = max(nums)  
        max_depth = len(bin(maxi)[2:])  
        t = Trie(max_depth)
        wanted_nums = []
        for i, num in enumerate(nums):
            qpp = bin(num)[2:]
            if max_depth == len(qpp):
                t.insert(num,qpp) 
                qpp = bin(((1<<max_depth)-1)^num)[2:] #因为先执行-后执行<< WA了一次
                wanted_nums.append((num,(max_depth-len(qpp))*'0'+qpp))
                if debug:
                    print(num, qpp, (max_depth-len(qpp))*'0'+qpp)
            else:
                t.insert(num, (max_depth-len(qpp))*'0'+qpp)

        for num,s in wanted_nums:
            t.search(num,s)
        return t.max_xor

        #Sol3.1 Trie优化2 没用class Trie 直接把insert/search都自己写了 但似乎一样都是1124ms 甚至还稍微慢了点
        debug = False
        maxi, max_xor = max(nums),0 
        max_depth = len(bin(maxi)[2:])  
        t = TrieNode()
        wanted_nums = []
        for i, num in enumerate(nums):
            qpp = bin(num)[2:]
            if max_depth == len(qpp):
                wanted_nums.append(num)
            cur = t
            for j in range(31, -1, -1):
                if debug: 
                    print((num & (1<<j))>>j,end="")
                cur = cur.children[(num & (1<<j))>>j]
            cur.num = num
            print(num)
        if debug:
            print(wanted_nums)
        for num in wanted_nums:
            cur = t
            for j in range(31, -1, -1):
                if debug:
                    print(j, cur.num, cur.children)
                idx = (num & (1<<j))>>j
                if cur.children.get(1-idx) is None:
                    cur = cur.children[idx]
                else:
                    cur = cur.children[1-idx]
            max_xor = max(max_xor, num^cur.num)
        return max_xor

        #Sol4 大神@Stefan的代码 128ms https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/91050/Python-6-lines-bit-by-bit
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer 
        '''key idea: answer += any(answer^1 ^ p in prefixes for p in prefixes)
        if (answer^1) XOR p matches Z in prefixes, 
        then p XOR Z matches (answer^1), which is what I am looking for. 
        p and Z are both elements in the prefix set.
        '''
        #Sol 4.1 看起来稍微清晰一咩咩
    def findMaximumXOR(self, nums):
        ans,debug = 0, True
        for i in reversed(range(32)):
            prefixes = set([x >> i for x in nums])
            ans <<=1
            candidate = ans + 1
            if debug: print("i: ",i," prefixes:", prefixes, " ans:",ans, " candidate:",bin(candidate))
            for p in prefixes:
                if debug: print(candidate ^ p, end=" ")
                if candidate ^ p in prefixes:
                    ans = candidate
                    break      
            print()
        return ans
'''
根据下面也可以看出来了 就是因为 x xor x = 0 所以之前的自己s.t.这个变为true了之后 后面的就不会in prefix 有待继续探讨啦
i:  31..5  prefixes: {0}  ans: 0  candidate: 0b1
1 
i:  4  prefixes: {0, 1}  ans: 0  candidate: 0b1
1 
i:  3  prefixes: {0, 1, 3}  ans: 2  candidate: 0b11
3 
i:  2  prefixes: {0, 1, 2, 6}  ans: 6  candidate: 0b111
7 6 
i:  1  prefixes: {1, 2, 4, 5, 12}  ans: 14  candidate: 0b1111
14 13 11 10 3 
i:  0  prefixes: {2, 3, 5, 8, 10, 25}  ans: 28  candidate: 0b11101
31 30 24 21 23 4 

'''
'''     自己最初乱乱的思考：
        每个word变成 应该是 前置0补全
        二叉树 end是固定的 或者用通用的也OK
        关键是返回最长匹配子串  不符合 提前break 符合的话 走到最后一步看看 
        其实最后一步可以直接记录是什么对不对 
        或者其实可以直接绑定此刻depth 所以其实是32n

'''



        #Sol1 O(n*n)
        max_xor, n = 0, len(nums)  # O(n*n) TLE
        for i in range(n):
            for j in range(i+1,n):
                max_xor = max(max_xor, nums[i]^nums[j])
        return max_xor

        #Sol2 bitwise的小优化
        max_xor, n = 0, len(nums) # max的话也可以到O(n*n) 我在想是可以利用absent搞一下 但是 嗯 有待考证吧～ 打算先叉出去做一下Trie看看
        xor = [[] for _ in range(31)]
        absent = [[] for _ in range(n)]
        for i,num in enumerate(nums):
            for j, c in enumerate(bin(num)[2:][::-1]):
                if c=='1':
                    xor[j].append(i)
                else:
                    absent[i].append(j)
        max_idx = 0 #RE了一次 因为没加这个 如果nums=[]  会 referenced before assignment
        for j in range(30,-1,-1):
            if len(xor[j])>0:
                max_idx = j
                break
        for i in xor[max_idx]:
            for j in range(n):
                max_xor = max(max_xor, nums[i]^nums[j])
        return max_xor

