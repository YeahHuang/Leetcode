import numpy as np
class Solution:
    def maxProfit(self, k:int, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        debug = False
        if n>=2 and k>0:
            k = min(n//2, k)
            buy, sell = [[-prices[i]]*k for i in range(n)], [[0]*k for _ in range(n)]
            #buy[0][0] = buy[0][1] = -prices[0]
            for i in range(1,n):               
                buy[i][0] = max(-prices[i], buy[i-1][0])
                sell[i][0] = max(prices[i]+buy[i-1][0], sell[i-1][0]) #一开始错误的把这里的+写成了- 
                for kk in range(1, k):
                    buy[i][kk] = max(sell[i-1][kk-1]-prices[i], buy[i-1][kk])
                    sell[i][kk] = max(prices[i]+buy[i-1][kk], sell[i-1][kk])
            if debug:
                print(np.transpose(buy))
                print(np.transpose(sell))
            
            max_profit = max(sell[n-1])
        return max_profit

        #RE了整整5次 包括没有考虑 k=0, k超级大 sell[i][kk]错误的写成了sell[i][0] 之类的情况
        #以及buy[0] = [0]*k 是不可行的 一定要在最最开始的时候好好定义
        #sample只是k=2 最好自己try了k>2&k=0/1的值再submit吖

    def maxProfit(self, k:int, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        debug = False
        if n>=2 and k>0:
            k = min(n//2, k)
            buy, sell = [-prices[i]]*k , [0]*k
            #buy[0][0] = buy[0][1] = -prices[0]
            for i in range(1,n): 
                sell[0] = max(prices[i]+buy[0], sell[0])
                buy[0] = max(-prices[i],buy[0])               
                for kk in range(1, k):
                    prev_buy, prev_sell = buy[kk], sell[kk-1]
                    buy[kk] = max(prev_sell-prices[i], buy[kk])
                    sell[kk] = max(prices[i]+prev_buy, sell[kk])
            if debug:
                print(np.transpose(buy))
                print(np.transpose(sell))
            
            max_profit = max(sell)
        return max_profit