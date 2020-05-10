# Python3 program to print all the cycles in an undirected graph 
from collections import defaultdict
UNVISITED = 0
VISITED = 1
FINISHED = 2
POPPED = 3

def dfs_cycle(u, p, state: list, mark: list, par: list): #给每个点染色 每个圈圈颜色不同
    global cyclenumber 

    if state[u] == FINISHED: 
        return

    if state[u] == VISITED: #找到一个没完成的但见过的点 -> cycle detected -> backtrack to find the complete cycle
        cyclenumber += 1
        cur = p 
        mark[cur] = cyclenumber 
        while cur != u:  #backtrack until it meets u 
            cur = par[cur] 
            mark[cur] = cyclenumber 
        return

    #这个点就是没见过 标注parent & state 即可 
    par[u] = p 
    state[u] = VISITED

    # simple dfs on graph 
    for v in adj[u]: 
        if v == par[u]: 
            continue
        dfs_cycle(v, u, state, mark, par) 

    # mark as completely visited. 
    state[u] = FINISHED


# Function to print the cycles 
def printCycles(n, mark: list, cycles): 

    # push the edges that into the 
    # cycle adjacency list 
    for i in range(1, n): 
        if mark[i] != 0: 
            cycles[mark[i]].append(i) 

    # print all the vertex with same cycle 
    for i in range(1, cyclenumber + 1): 

        # Print the i-th cycle 
        print("Cycle Number %d:" % i, end = " ") 
        for x in cycles[i]: 
            print(x, end = " ") 
        print() 


# variables to be used 
# in both functions 
n = 14
adj = defaultdict()
adj[1] = [2]
adj[2] = [1,3]
adj[3] = [2,4,5]
adj[4] = [3,7,6]
adj[5] = [3,6,9]
adj[6] = [4,5,10]
adj[7] = [4,8]
adj[8] = [7]
adj[9] = [5]
adj[10] = [6, 11]
adj[11] = [10, 12, 13]
adj[12] = [11,13]
adj[13] = [11, 12]

cycles = [[] for _ in range(n)]

state = [0] * n
par = [0] * n
mark = [0] * n #记录cycle number的
cyclenumber = 0

# call DFS to mark the cycles 
dfs_cycle(1, 0, state, mark, par) 

# function to print the cycles 
printCycles(n, mark, cycles) 

# This code is contributed by 
# sanjeev2552 
