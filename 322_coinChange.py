class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAXN = amount+1
        f = [MAXN]*(amount+1)
        f[0] = 0
        for i in range(1, amount+1):
            f[i] = min([f[i-coin] if i>=coin and f[i-coin]!=MAXN else MAXN-1 for coin in coins]) + 1
        return f[amount] if f[amount]!=MAXN else -1 

#Improved: MAXN = amount + 1 -> float('inf') 1264ms->892ms beats90%
#Further Improved： 用滚动数组优化空间
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAXN = float('inf') #最大值好像还是直接用这个定义更好一点 可以不用烦MAXN-1 +1 什么奇怪的东西
        f = [MAXN]*(amount+1)
        f[0] = 0
        for i in range(1, amount+1):
            f[i] = min([f[i-coin] if i>=coin else MAXN for coin in coins]) + 1
        return f[amount] if f[amount]!=MAXN else -1 
