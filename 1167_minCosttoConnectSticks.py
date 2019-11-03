class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        ret = 0
        while len(sticks) > 1:
            p1, p2 = heapq.heappop(sticks), heapq.heappop(sticks)
            ret += (p1+p2)
            heapq.heappush(sticks, p1+p2)
        return ret
    #beats 39% 几乎是标准答案 但我把最快的代码(360ms vs 339ms)跑了我这儿 反而慢了(372ms) anyway no worries