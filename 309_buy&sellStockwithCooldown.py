class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy sell cooldown gap 
        #last sell + min 其实buy的状态根本不重要的 
        n = len(prices)
        max_profit = 0
        if n>0:
            f = [0] * n
            for i in range(1,n):
                f[i] = f[i-1]
                for j in range(i):
                    if prices[j]<prices[i]:
                        f[i] = max(f[i], prices[i]-prices[j] + (f[j-2] if j>=2 else 0))
            max_profit = f[n-1]
            #print(f)
        return max_profit

        #p.s. 当你发现推不出与n-1的关系的时候 一定要多加状态 rest buy sell 一眼望到头的但是不可延展的不如多加状态的好啊
        n = len(prices)
        max_profit = 0
        if n>0:
            f = [0] * n
            buy, sell, rest = [0] * n, [0] * n, [0] * n
            buy[0] = -prices[0]
            for i in range(1,n):
                #buy[i] = max(-prices[i], buy[i-1]) #表示至少有一个买的状态 传递的感觉好像还是没有想清楚 这里传递就通过rest了
                buy[i] = max(rest[i-1]-prices[i], buy[i-1])
                sell[i] = max(sell[i-1], buy[i-1]+prices[i])
                rest[i] = max(sell[i-1], rest[i-1])
            max_profit = max(sell[n-1],rest[n-1])
        return max_profit

        #别人的 空间O(1):
        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        return max(notHold, notHold_cooldown)