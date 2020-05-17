class Solution:
    #一开始想着 啊 那和trapping water1 一样 四个方向取一个min就好啦
    #但会WA 因为candidate除了四个方向 还有更多 需要用visited + heap记录会更快
    # Input： [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
    # output： 15 我的WA在于认为4的height是13 其实只有12
    # expected： 14


    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        left_most, right_most, up_most, down_most = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)], [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
        water_volumn = 0 
        for i in range(m):
            for j in range(n):
                left_most[i][j] = max(left_most[i][j-1] if j>0 else 0, heightMap[i][j])
                up_most[i][j] = max(up_most[i-1][j] if i>0 else 0, heightMap[i][j])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                right_most[i][j] = max(right_most[i][j+1] if j<n-1 else 0, heightMap[i][j])
                down_most[i][j] = max(down_most[i+1][j] if i<m-1 else 0, heightMap[i][j])
        print(left_most[2],right_most[2])
        print(up_most[2], down_most[2])
        for i in range(1,m-1):
            for j in range(1,n-1):
                if heightMap[i][j] > max(left_most[i][j-1], up_most[i-1][j], right_most[i][j+1], down_most[i+1][j]):
                    water_volumn += min(left_most[i][j-1], up_most[i-1][j], right_most[i][j+1], down_most[i+1][j])
        return water_volumn

    #take a look at https://leetcode.com/problems/trapping-rain-water-ii/discuss/89472/Visualization-No-Code
    #Python's heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]):
           
        if not heightMap or not heightMap[0]:
            return 0
        
        import heapq    
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0]*n for _ in range(m)]

        # Push all the block on the border into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        
        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)    
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height-heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y)) 
                    #本以为如果 heightMap[x][y]< height 也可以不push 不是这样的 会WA 呜呜呜 大概新的边界还是要继续推行啊
                    visited[x][y] = 1
        return result
        