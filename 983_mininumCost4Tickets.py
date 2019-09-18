class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #f = len(days)* gap >= 15的必然重新开
        #主要问题是到这里是否有寸余如果用连续的来解决这个问题似乎可行。 判断绑定/重开 
        MAXN = float('inf')
        days.sort()
        start = [[MAXN]*3 for _ in range(len(days))] #0-1days 1-2days 2-3days
        end = [MAXN] * len(days)
        for i, day in enumerate(days):
            for j in range(3):
                start[i][j] = (end[i-1] if i>=1 else 0) + costs[i]
            end[i] = min(start[i])
            for j in range(i-1, -1, -1):
                if days[i] - days[j] >= 15:
                    break
                end[i] = min(end[i], start[j][2])
                if days[i] - days[j] < 7:
                    end[i] = min(end[i], start[j][1])
        return end[-1]