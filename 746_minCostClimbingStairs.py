class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost) 
        ans = [0] * (n*3)
        ans[0] = cost[0]
        ans[1] = cost[1]
        for i in range(2,n):
            ans[i] = min(ans[i-1],ans[i-2]) + cost[i]
        return min(ans[n-1],ans[n-2])  
        #一开始错误的写成了return ans[n-1] 看到类似&简单的题目不要太开心哦 谨慎谨慎谨慎 认真读题