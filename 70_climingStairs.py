class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * (n+3)
        f[1] = 1
        f[2] = 2
        for i in range(3,n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]