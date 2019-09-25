class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0: 
            return 0
        f = [0] * (n+1)  #f[i] stores ways of (i)
        f[0] = f[1] = 1
        for i in range(2, n+1): 
            for j in range(1, i+1):
                f[i] += f[i-j] * f[j-1]
        return f[-1]
        #符合Catalan number 所以可以 直接 以下：
    def numTrees(self, n):
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
        #或 return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))