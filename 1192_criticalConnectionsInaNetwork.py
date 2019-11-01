import collections
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dfn, low, father = [-1]*n, [-1]*n, [-1]*n
        t = collections.defaultdict(list)
        self.time_stamp = 0
        for c in connections:
            t[c[0]].append(c[1])
            t[c[1]].append(c[0])
        ret = []

        def dfs(idx):
            self.time_stamp += 1 #WA一次 一开始以为可以自动默认global了 结果还是需要加self. 的
            low[idx] = dfn[idx] = self.time_stamp 
            for child in t[idx]:
                if dfn[child]==-1:
                    father[child] = idx
                    dfs(child)
                if child != father[idx]:
                    low[idx] = min(low[idx], low[child])
        '''
        我尝试把father[] 用单一的father代替，结果时间2524 -> 2412  81.9 -> 81.6 
        def dfs(idx, father):
            self.time_stamp += 1
            low[idx] = dfn[idx] = self.time_stamp
            for child in t[idx]:
                if dfn[child]==-1:
                    dfs(child, idx)
                if child != father:
                    low[idx] = min(low[idx], low[child])
        '''

        dfs(0)
        #print(dfn, low, father)
        for c in connections:
            #if (dfn[c[0]] - dfn[c[1]]) * (low[c[0]] - low[c[1]]) > 0: #WA 一次 一开始弄错了
            if low[c[0]] > dfn[c[1]] or low[c[1]]>dfn[c[0]]:
                ret.append(c)
        return ret