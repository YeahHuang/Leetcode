import numpy as np
class Solution:
    def maxProfit(self, k:int, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        debug = False
        if n>=2 and k>0:
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

    #为了解决MLE 的improvd version:
    def maxProfit(self, k:int, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        debug = False
        if n>=2 and k>0:
            if k >= n / 2: #如果不加这个的话就会TLE 真的很巧妙啊 因为连续的可以直接合并 肯定不会被浪费的
                return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
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
            max_profit = max(sell)
        return max_profit

    '''
    继续优化：
    python：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/298738/Python-solution-faster-than-99.5-with-full-analysis
    C++：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54118/C%2B%2B-Solution-with-O(n-%2B-klgn)-time-using-Max-Heap-and-Stack
     1. 结合上面的连续的可以直接合并 
     2. 其实只需要每次找一个p(t+1) - p(t)的最小值即可
    for i in range(0, len(prices)):
    if buying and (i != len(prices)-1 and prices[i+1] > prices[i]):
      opt_prices.append(prices[i]); buying = False
    else:
      if not buying and (i == len(prices)-1 or prices[i+1] < prices[i]): 
        opt_prices.append(prices[i]); buying = True
  return opt_prices

def merge(prices):
  best_merge = 0
  best_merge_cost = sys.maxsize

  for i in range(0, len(prices)-1):
    if abs(prices[i+1] - prices[i]) < best_merge_cost:
      best_merge = i
      best_merge_cost = abs(prices[best_merge+1] - prices[best_merge])

  del(prices[best_merge : best_merge+2])

def simpleSum(prices):
  sum = 0
  for i in range(0, len(prices), 2):
    sum += prices[i+1] - prices[i]
  return sum

def maxProfit(self, k: int, prices: List[int]) -> int:
    if (k == 0):
      return 0

    opt_prices = Solution.getPriceReversals(prices)

    while len(opt_prices)/2 > k:
        Solution.merge(opt_prices)
        
    return Solution.simpleSum(opt_prices)




