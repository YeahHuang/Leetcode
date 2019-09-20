class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        dic = {} 
        for x, y in points: 
            if x in dic:    #可以定义dic = collections.defaultdict(set) 这儿就可以不用特别判断啦
                dic[x].add(y)
            else:
                dic[x] = {y}
        xx = sorted(dic.keys())
        minArea = float('inf')
        for i in range(len(xx)):
            for j in range(i+1, len(xx)):
                inter = dic[xx[i]] & dic[xx[j]]
                if len(inter) >= 2:
                    tmp = sorted(list(inter)) 
                    minArea = min(minArea, min([tmp[k+1]-tmp[k] for k in range(len(tmp)-1)])*(xx[j]-xx[i]))
        return minArea if minArea<float('inf') else 0

    #Improved：896 -》 228 把set &  lastx[y1,y2] = x
    def minAreaRect(self, points):
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0
        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x #精妙的最后一步 会比我的set & 快
        return res if res < float('inf') else 0