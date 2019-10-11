class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        #dp[N][N] = n!
        #dp[N][N+1] = dp[N][L]*(N-K)+ dp[N-1][L]*N
        MOD = int(1e9 + 7)
        f = [[0]*(L+1) for i in range(N+1)]
        f[0][0], f[1][1] = 1, 1
        for i in range(2, K+1):
            f[i][i] = (f[i-1][i-1]*i)%MOD #f[i][i] = math.factorial(i)
        for i in range(K+1, N+1): 
            f[i][i] = (f[i-1][i-1]*i)%MOD
            for j in range(i+1, L+1):
                f[i][j] = (f[i][j-1]*(i-K)%MOD + f[i-1][j-1] * i % MOD)%MOD
            #print(f[i])
        return f[-1][-1]