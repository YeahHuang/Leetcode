class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int: 
    #最后差的临门一脚是考虑如果不是(K-1) 的倍数怎么办
    #优化前也可以考虑 stones[l][r][m] [l,r] into m piles 总之dp推导不出来的时候就增加参数维度试一试吖 

        if len(stones)==1:
            return 0
        if (len(stones)-1)%(K-1)!=0 : #WA in [1] 2
            return -1
        merge_times = (len(stones)-1)//(K-1)
        self.memo = {}
        self.prefix = [0]
        for s in stones:
            self.prefix.append(self.prefix[-1] + s)
        return self.dfs(stones, 0, len(stones)-1, K)

    def dfs(self, stones, l, r, K):
        if (l,r) in self.memo: #把memo去掉 反而 64ms -> 60ms
            return self.memo[(l,r)]
        if r-l+1 < K:
            return 0
        ret = float('inf')
        for mid in range(l, r, K-1):
            ret = min(ret, self.dfs(stones, l, mid, K) + self.dfs(stones, mid+1,r,K))
        if (r-l) % (K-1) == 0:
            #ret += sum(stones[l:r+1])
            ret += self.prefix[r+1]-self.prefix[l]
        self.memo[(l,r)] = ret
        return ret

#Sol referenced from @lee215 56ms
    def mergeStones(self, stones, K):
        n = len(stones)
        if (n - 1) % (K - 1): return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K: return 0
            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))
            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]
            return res
        return dp(0, n - 1)
    

class Solution: #WA因为我是根据 k=3 从头开始想的 最大的point 就是 如果不是它的倍数的话 就不加 直接combine就是了～ 
    def mergeStones(self, stones: List[int], K: int) -> int:
        if len(stones)==1:
            return 0
        if (len(stones)-1)%(K-1)!=0 : #WA in [1] 2
            return -1
        merge_times = (len(stones)-1)//(K-1)
        self.memo = {}
        self.debug = True
        return self.dfs(stones, 0, len(stones)-1, merge_times, K)

    def dfs(self, stones: List[int], l, r, merge_times, K: int) -> int:
        if self.debug:
            print(l, r, merge_times, K)
        if (l,r) in self.memo:
            return self.memo[(l,r)]
        if (r-l+1 - 1)%(K-1)!=0 or (r-l)//(K-1)!=merge_times:
            print("ERROR!, ",l,r,(r-l+1 - 1)%(K-1), merge_times)
            return -1 
        #merge_times = (r-l)//(K-1)
        ret = sum(stones[l:r+1])
        if merge_times == 1:
            self.memo[(l,r)] = ret
            return ret
        min_rec = float('inf')
        for i in range(l, l+K):
            min_rec = min(min_rec, self.dfs(stones, i, i + r - l - K, merge_times-1, K))
        if merge_times > 2:
            min_rec = min(min_rec, self.dfs(stones, l, r-K, merge_times-2, K)+sum(stones[r-K+1: r+1]), \
                                self.dfs(stones, l+K, r, merge_times-2, K) + sum(stones[l: l+K]))
        ret += min_rec
        self.memo[(l,r)] = ret
        if self.debug:
            print(l, r, merge_times, K, ret)
        return ret

class Solution: #WA
    def mergeStones(self, stones: List[int], K: int) -> int:
        if len(stones)==1:
            return 0
        if (len(stones)-1)%(K-1)!=0 : #WA in [1] 2
            return -1

        n = len(stones)
        merge_times = (len(stones)-1)//(K-1) #合并次数
        dp = [[0]*n for _ in range(merge_times+1)]
        dp[1][:n-K+1] = [sum(stones[i:i+K]) for i in range(n-K+1)]
        for times in range(2,merge_times+1):
            tmp = times*(K-1)
            #print(tmp) 
            for start_idx in range(n-tmp):
                print(times, start_idx,dp)
                dp[times][start_idx] = min(dp[times-1][k] for k in range(start_idx, start_idx+K)) \
                                        + sum(stones[start_idx: start_idx+tmp+1])
                if times > 2:
                    dp[times][start_idx] = min(dp[times-2][start_idx+K]+sum(stones[start_idx: start_idx+K]),\
                                             dp[times-2][start_idx] + sum(stones[-K:]))\
                                              + sum(stones[start_idx: start_idx+tmp+1])

        #print(dp)
        
        return dp[-1][0]

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        if len(stones)==1:
            return 0
        if (len(stones)-1)%(K-1)!=0 : #WA in [1] 2
            return -1
        merge_times = (len(stones)-1)//(K-1)
        self.memo = {}
        prefix = [0]
        for s in stones:
            prefix.append(prefix[-1] + s)
        return self.dfs(stones, 0, len(stones)-1, K)

        @functools.lru_cache(None)
        def dfs(self, stones, l, r, K):
            if (l,r) in self.memo:
                return self.memo[(l,r)]
            if r-l+1 < K:
                return 0
            ret = float('inf')
            for mid in range(l, r, K-1):
                ret = min(ret, self.dfs(stones, l, mid, K) + self.dfs(stones, mid+1,r,K))
            if (r-l) % (K-1) == 0:
                #ret += sum(stones[l:r+1])
                ret += prefix[r+1]-prefix[l]
            self.memo[(l,r)] = ret
            return ret
