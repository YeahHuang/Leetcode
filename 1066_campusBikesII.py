class Solution:
    def assignBikes(self, workers, bikes):
        #Sol1 brute force 不要害怕暴力 面试的时候其实很多时候如果你能快速想到暴力的解法也很棒的 会tle
        N, M = len(workers), len(bikes)
        global min_dist, dist 
        dist = [[-1]*M for _ in range(N)]
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist[i][j]=abs(worker[0]-bike[0])+abs(worker[1]-bike[1])
        min_dist = 2000*N
        
        def dfs(work_idx, used_bikes, cur_dist):
            global min_dist, dist #一开始忘记写global了
            if cur_dist<min_dist and work_idx<=N:
                if work_idx == N:
                    min_dist = cur_dist
                else:
                    for i in range(M):
                        if used_bikes[i] == False:
                            used_bikes[i] = True
                            dfs(work_idx + 1,  used_bikes, cur_dist + dist[work_idx][i])
                            used_bikes[i] = False
        dfs(0, [False]*M, 0)
        return min_dist


        #Sol2 状压DP 400ms
        N, M = len(workers), len(bikes)
        dist = [[-1]*M for _ in range(N)]
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist[i][j]=abs(worker[0]-bike[0])+abs(worker[1]-bike[1])
        
        MAX_DIST = 2000*N
        dp = [[MAX_DIST]*(1<<M) for i in range(N+1)]
        dp[0][0] = 0 
        for i in range(N):
            for s in range(1, 1<<M):
                for j in range(M):
                    if s&j>0: #not visited 
                        dp[i+1][s] = min(dp[i+1][s], dp[i][s-(1<<j)]+dist[i][j])
        return min(dp[i])

        #Sol3 关于状态转化 我在for s in range(1, 1<<M)的前面步骤里其实有很多无效步骤 400ms -> 128ms
        #Referenced from @Lee215
        def dis(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        h = [[0, 0, 0]]
        #heapq.heapify(h) 这里只有一个元素 可以不用heapify
        seen = set()
        while True:
            cost, i, taken = heapq.heappop(h)
            if (i, taken) in seen: continue
            seen.add((i, taken))
            if i == len(workers):
                return cost
            for j in range(len(bikes)):
                if taken & (1 << j) == 0:
                    heapq.heappush(h, [cost + dis(i, j), i + 1, taken | (1 << j)])
