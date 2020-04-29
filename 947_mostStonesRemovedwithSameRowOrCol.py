#Sol1 Union Find 连接两个list 染色问题 188ms
class DSU: #Disjoint Set Union 就是常见的染色问题
    def __init__(self):
        self.p = {}

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p.setdefault(x,x)
        self.p.setdefault(y,y)
        self.p[self.find(x)] = self.p[self.find(y)]

class Solution:
    def removeStones(self, stones):
        dsu = DSU()
        for x,y in stones:
            dsu.union(x, ~y)
        islands = len(set([dsu.find(x) for x, y in stones])) 
        #这里本来也需要set(dsu.find(x),dsu.find(y)) 但因为前面的东西保证二者必然相同 所以省略
        return len(stones) - islands

#sol1.1 188ms -> 172ms 而且内存基本没变 
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

    def union(self, x, y):
        self.p.setdefault(x,x)
        self.sz.setdefault(x,1)
        self.p.setdefault(y,y)
        self.sz.setdefault(y,1)
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

#Sol2 dfs 156ms
class Solution:
    def removeStones(self, stones):
        x, y = collections.defaultdict(list), collections.defaultdict(list)
        for i, (xx, yy) in enumerate(stones):
            x[xx].append(i)
            y[yy].append(i)
        seen = [False] * len(stones)
        islands = 0 
        for i, (xx, yy) in enumerate(stones):
            if seen[i]==False:
                seen[i] = True
                islands += 1
                stack = [i]
                while stack:
                    idx = stack.pop()
                    for j in x[stones[idx][0]]:
                        if seen[j] == False:
                            seen[j] = True
                            stack.push(j)
                    for j in y[stones[idx][1]]:
                        if seen[j] == False:
                            seen[j] = True
                            stack.push(j)
        return len(stones) - islands

    def removeStones(self, stones: List[List[int]]) -> int:
        '''
        一开始这就是没规划好 写的冗余的不得了 其实 x，y都不用的
        x, y = collections.defaultdict(list), collections.defaultdict(list)
        for i, (xx, yy) in enumerate(stones):
            x[xx].append(i)
            y[yy].append(i)
        #print(x)
        lenx, leny = {},{}
        for xx, l in x.items():
            lenx[xx] = len(l)
        for yy, l in y.items():
            leny[yy] = len(l)
        '''
        lenx, leny = {},{}
        for i, (xx, yy) in enumerate(stones):
            lenx[xx] = lenx.get(xx, 0) + 1
            leny[yy] = leny.get(yy, 0) + 1
            
        cnt = 0

        while stones:
            new = []
            mini = float('inf')
            j = 0 
            for i, (xx, yy) in enumerate(stones):
                if lenx[xx] + leny[yy] > 2:
                    new.append([xx,yy])
                    if lenx[xx] + leny[yy] < mini:
                        mini = lenx[xx] + leny[yy] 
                        idx = j
                    j += 1
                else:
                    lenx[xx] -= 1
                    leny[yy] -= 1
                    
            if j == 0:
                break
            lenx[new[idx][0]] -= 1
            leny[new[idx][1]] -= 1
            #print("is popping",idx, new)
            #print(lenx, leny)
            new.pop(idx)
            stones = new
            cnt += 1
        return cnt
            
        '''
        degree = []
        for i, (xx, yy) in enumerate(stones):
            degree.append(lenx[xx] + leny[yy], xx, yy)
            if degree[i][0]==2:
                degree[i][0] = float('inf')
        degree.sort()
        while degree and degree[0][0]<float('inf'):
            _, xx, yy = degree.pop(0) #(xx, yy)里的都要pop degree - 1
            for i in x[xx]: #你会发现这儿degree的编号也变了 所以这个方法不是很可行的
        '''