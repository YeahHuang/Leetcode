class Solution:

    #Sol1 sort NlgN
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist,debug = [],True
        for i,(x,y) in enumerate(points): #用dist = lambda i: points[i][0]**2 + points[i][1]**2 来优化吖
            dist.append((x*x + y*y,i))
        dist.sort()
        if debug:
            print(dist)
        return [points[dist[i][1]] for i in range(K)]

        #Sol1.2 改进版 lambda的使用还需要更加熟练吖
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]

    #Sol2 类似quick-sort的divide&conquer
    class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def pivotFind(l, r, k):
            if l >= r:
                return
            debug = True
            qpp = random.randint(l,r) #这里不记得了 要注意呀
            pivot = dist(qpp)
            points[l],points[qpp] = points[qpp],points[l]
            i, j = l+1, r
            while True:
                while i<j and dist(i) < pivot:
                    i += 1
                while i<=j and dist(j) >= pivot:
                    j -= 1
                if i>=j: break
                points[i], points[j] = points[j], points[i]
                
            points[l], points[j] = points[j],points[l]
            if j-l+1==k:  #这里一开始写成了i==k, i>k 注意是i和l的关系呀
                if debug:
                    print(i,l,k,j-l+1)
                #return points[:k]
            elif j-l+1>k:
                pivotFind(l,j-1, k)
            else:
                pivotFind(j+1,r, k-(j-l+1)) #一开始写成了pivotFind(i+1,r, k-i)  明显没有真的认真思考吖

        pivotFind(0, len(points)-1, K)
        return points[:K]
