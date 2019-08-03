class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        if n>0:
            f = [0] * n
            buy, sell, rest = [-prices[0]], [0], [0]
            for i in range(1,n):               
                buy.append(max(sell[i-1]-prices[i], buy[i-1])) #表示end with buy的状态 
                sell.append(max(sell[i-1], buy[i-1]+prices[i])) #表示end with sell的状态 
            max_profit = sell[n-1]
        return max_profit