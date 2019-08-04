class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        if n>=2:
            buy, sell = [[0]*2 for _ in range(n)], [[0]*2 for _ in range(n)]
            buy[0][0] = buy[0][1] = -prices[0]
            for i in range(1,n):               
                buy[i][0] = max(-prices[i], buy[i-1][0])
                sell[i][0] = max(prices[i]+buy[i-1][0], sell[i-1][0]) #一开始错误的把这里的+写成了- 
                buy[i][1] = max(sell[i-1][0]-prices[i], buy[i-1][1])
                sell[i][1] = max(prices[i]+buy[i-1][1], sell[i-1][1])
            max_profit = sell[n-1]
        return max_profit

        #p.s. 这里其实可以把sell[i][k] 的k从0，1 引申到更多次 因为对应的sell[i][k] 仅仅与sell[i][k-1]相关