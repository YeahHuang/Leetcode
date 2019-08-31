class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        dist = []
        N, M = len(workers), len(bikes)
        flag_workers, flag_bikes, ans = [True] * N, [True]*M, -1*N
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist.append((abs(worker[0]-bike[0])+abs(worker[1]-bike[1]), i, j))
        dist.sort()
        for d in dist: 
        #这里用 for d, worker, bike in dist 会好理解很多 
        #这里还可以设置 判断ans[worker_idx]==-1 和 bike_taken = set() 来方便节省空间～
            if flag_workers[d[1]] and flag_bikes[d[2]]:
                ans[d[1]] = d[2]
                flag_bikes[d[1]]= flag_bikes[d[2]] = True
        return ans 


    #Sol2 Referenced from @yorkshire's Sol 1828ms -> 792ms
    def assignBikes(self, workers, bikes):
        N, M = len(workers), len(bikes)
        dist,ans = [[] for _ in range(N)], [-1]*N
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist[i].append((abs(worker[0]-bike[0])+abs(worker[1]-bike[1]), i, j))
            dist[i].sort(reverse=True)
        queue = [dist[i].pop() for i in range(N)]
        heapq.heapify(queue)
        used_bikes = set()
        #for i in range(N): WA一次 要用下面这个巧妙的判断方式哦
        while len(used_bikes)<N:
            _,  worker_idx, bike_idx = heapq.heappop(queue)
            if bike_idx in used_bikes:
                heapq.heappush(queue, dist[worker_idx].pop())
            else:
                ans[worker_idx] = bike_idx
                used_bikes.add(bike_idx)
        return ans