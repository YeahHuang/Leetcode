class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #Sol1 我其实都到了强连通图的知识 有点小题大做的意思 anyway 不到40minKO 一次AC还是不错的了～
        #76ms
        def findFather(num):
            if father[num]==num:
                return num
            else:
                father[num] = findFather(father[num])
                return father[num]

        father = {}
        consecutive_num = {}
        debug = False
        for num in nums:
            if num in father.keys(): #这个直接一开始num_set = set(nums) 就可以全过滤掉 更快
                print("Note! there can be duplicates")
                continue
            p1 = num-1 in father.keys()  #这两行提炼出来其实没啥意义 速度还会76ms -> 80ms 变慢
            p2 = num+1 in father.keys()
            if p1 and p2:
                f1 = findFather(num - 1)
                f2 = findFather(num + 1)
                consecutive_num[f1] += consecutive_num[f2] + 1
                father[num] = f1
                father[f2] = f1
                consecutive_num.pop(f2)
            elif p1:    #其实如果没有陷入强连通的姿势的话是很快的 
                father[num] = findFather(num - 1)
                consecutive_num[father[num]] += 1
            elif p2:
                father[num] = findFather(num + 1)
                consecutive_num[father[num]] += 1
            else:
                father[num] = num
                consecutive_num[num] = 1
            if debug:
                print("num=",num," father:",father,"consecutive_num:",consecutive_num)
        ans = 0
        for k,v in consecutive_num.items():
            ans = max(ans, v)
        return ans 

    #Sol2 72ms
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur_num = num + 1
                while cur_num in nums_set:
                    cur_num += 1
                ans = max(ans, cur_num - num)
        return ans

    #Sol3 76ms 把前面后面在里头的remove的思想挺好的 虽然其实和sol2一样本质上都是利用set啦
    def longestConsecutive(self, nums):
        nums = set(nums)
        maxlen = 0
        while nums:
            first = last = nums.pop()
            while first - 1 in nums:
                first -= 1
                nums.remove(first)
            while last + 1 in nums:
                last += 1
                nums.remove(last)
            maxlen = max(maxlen, last - first + 1)
        return maxle

#sol4 4.28 update 用union find (类似于sol1) 84ms
class DSU: #Disjoint Set Union 就是常见的染色问题
    def __init__(self):
        self.p = {}
        self.sz = {}

    def find(self, x):

        stack = []
        while self.p[x] != x:
            stack.append(x)
            x = self.p[x]
        for xx in stack:
            self.p[xx] = x
        '''
        if self.p[x] != x: 会MLE
            self.p[x] = self.find(self.p[x])
        '''
        return x

    def union0(self, x):
        self.p.setdefault(x,x)
        self.sz.setdefault(x, 1)   
        if x - 1 in self.p.keys():
            self.union(x,x-1)
        if x + 1 in self.p.keys():
            self.union(x, x+1)
            
    def union(self, x, y):

        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.sz[px] < self.sz[py]:
            self.sz[py] += self.sz[px]
            self.p[px] = self.p[py]
        else:
            self.sz[px] += self.sz[py]
            self.p[py] = self.p[px]
        return True
    


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dsu = DSU()
        if len(nums)==0:
            return 0
        for num in nums:
            if num not in dsu.p.keys():
                dsu.union0(num)
        for num in nums:
            dsu.find(num)
        return max(dsu.sz.values())