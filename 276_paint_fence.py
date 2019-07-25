class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0: return 0 
        f = [[1,k-1] for _ in range(n+1)] #0 equals 1 not equals
        f[1] = [k, k*(k-1)] #Attention：这是基于n>=2的基础上的
        #一开始把non-negative错误的和此对等 没有核查 n = 0, 1 的情况 WA
        for i in range(2,n):
            f[i][0] = f[i-1][1] * 1
            f[i][1] = (f[i-1][0]+f[i-1][1])*(k-1)
        return sum(f[n-1])

    #一开始错误的写成了 k * ((k-1)**(n-1))