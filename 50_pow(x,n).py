class Solution:
    def myPow(self, x: float, n: int) -> float:
        #Sol1 x**n O(n)
        #Sol2 O(nlgn)

        if n<0:         #这里没办法改 但可以学一下 m = -n if n<0 else n 这样的用法
            x = 1/x
            n = -n

        def pow(x, n):
            debug = False
            if n == 0:
                ans = 1 
            elif n == 1:
                ans = x
            #这俩位运算都加上 可以40ms -> 36ms
            elif n%2==0:    #改成 n & 1 更酷
                ans = pow(x, n//2) ** 2 #改成 n >> 1 更酷
            else:
                ans = x*(pow(x, n//2) ** 2)
            if debug:
                print(x, n, ans)
            return ans

        return pow(x,n)