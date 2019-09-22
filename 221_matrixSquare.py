class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxi = 0
        if len(matrix)==0: return 0
        m, n = len(matrix), len(matrix[0])
        t = [[(0,0)] * n for _ in range(m)]
        for i in range(m-1, -1 , -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    t[i][j] = (t[i+1][j][0] if i+1<m else 0)+1, (t[i][j+1][1] if j+1<n else 0)+1
                    maxi = 1
        for i in range(m):
            for j in range(n):
                if min(t[i][j]) > maxi:
                    cur = t[i][j][1]
                    for k in range(i+1, i+min(t[i][j])):
                        cur = min(cur, t[k][j][1])
                        if cur<=maxi:
                            break
                        elif k-i+1>maxi:
                            maxi = max(maxi, min(k-i+1, cur))
        return maxi**2

    #Sol2O @Stefan 最快的 但是似乎比起我的也仅仅是228->196ms 看来少量dp+优秀的剪枝效果也不错滴 
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            matrix[i] = list(map(int, matrix[i])) #python2可以直接map python3需要转化为list才能具有list效果 但下面的max(map...) 就不用转
            for j in range(len(matrix[i])):
                if i and j and matrix[i][j]:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
        return len(matrix) and max(map(max, matrix))**2 #或者return max(map(max, A + [[0]])) ** 2
