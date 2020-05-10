#referenced and modified from https://cims.nyu.edu/~brettb/dsSum2016/Lecture19.pdf
from collections import defaultdict
class TarjanSCC:
    UNVISITED = 0
    VISITED = 1
    FINISHED = 2
    POPPED = 3
    def __init__(self,adj): #输入邻接矩阵 adj 是一个key为0..n 的defaultdict
        n = len(adj)
        self.num = 0
        self.state = [0] * n
        self.dfsNum = [0] * n   #相当于时间戳timestamp
        self.dfsLow = [0] * n
        self.stack = []
        for v in range(n):
            self.tarjanSCC(adj, v, self.state, self.dfsNum, self.dfsLow, self.stack)

    def tarjanSCC(self, adj, v, state, dfsNum, dfsLow, stack):
        if state[v] != self.UNVISITED:
            return dfsLow[v]
        #Whennever a new vertex v is visted
        state[v] = self.VISITED      
        dfsNum[v] = self.num #update v's timestamp
        self.num += 1
        dfsLow[v] = dfsNum[v] #initialize dfsLow[v] = dfsNum[v] 
        stack.append(v) #push v into stack
 
        #Then traverse all its neighbors to update dfsLow[v] = min(dfsLow[w] where w is v's unpopped neighbours)
        for w in adj.get(v): 
            if state[w] == self.POPPED:
                continue
            wNum = self.tarjanSCC(adj, w, state, dfsNum, dfsLow, stack)
            dfsLow[v] = min(dfsLow[v], wNum)

        #After traverse mark as finished
        state[v] = self.FINISHED

        #Check if there is SCC
        if dfsLow[v] >= dfsNum[v]:
            scc = []
            while True:
                w = stack.pop() #这里其实可以记录一下w的 因为所有pop出去的 就是我们需要的SCC
                state[w] = self.POPPED
                scc.append(w)
                if w == v:
                    break
            print("scc: ", scc)
        return dfsLow[v]

adj = defaultdict()
adj[0] = [1,2]
adj[1] = [3]
adj[2] = [5,6]
adj[3] = [4]
adj[4] = [1]
adj[5] = [1,7]
adj[6] = [5]
adj[7] = [2]
tarjan = TarjanSCC(adj)

print(tarjan.dfsNum)


