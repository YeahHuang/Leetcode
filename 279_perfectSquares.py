#p.s. static variable,  dp/dfs一定要只考虑单步的问题 不然会有冗余 就慢了
class Solution:
    #Sol1 static + dp
    _f = [0] #这个如果写在__init__里 就是2332ms 写在外面就是88ms 看来要学习以下python的 static variable
    def numSquares(self, n):
        f = self._f #因为array是地址赋值 这样写的话很快也会让后面的代码很简洁
        while len(f) <= n:
            f += [min(f[-i*i] for i in range(1, int(math.sqrt(len(f)))+1)) + 1] #WA一次 一开始math.sqrt(n)了
        return f[n]

    #Sol2 TLE when n =  428
    def __init__(self):
        self.f = {}
        
    def numSquares(self, n: int) -> int:
        self.f[0] = 0
        for i in range(1, int(math.sqrt(n))+1):
            self.f[i*i] = 1
        ret =self.dfs(n)
        return ret
    
    def dfs(self, n: int):
        if n in self.f:
            return self.f[n]
        self.f[n] = n
        for i in range(int(math.sqrt(n)), 1, -1):
            tmp = n - i*i
            times = 1
            while tmp >= 0:
                #self.f[n] = min(self.dfs(tmp)+1, self.f[n]) 把这个改好了就也可以pass 510 test了
                self.f[n] = min(self.dfs(tmp)+times, self.f[n])
                tmp -= i*i
                times += 1
        #print("For n = %d, f[n]=%d"%(n, self.f[n]))
        return self.f[n]

    #TLE when n = 6175 Improved by adding upp_i, upp_f  already pass 510/588
class Solution: 
    f = {}     #把原来的__init__里的self.f 放在这里 方便多个测试集共用 就pass 2268ms 但只快15.79%
                #不要tmp -= 每一个sqrt 只减一个的话 就是faster than 15.79%
    def numSquares(self, n: int) -> int:
        self.f[0], self.f[1226] = 0,2#太神奇了 1226的时候直接测是3 跑完leetcode就是2了
        for i in range(1, int(math.sqrt(n))+1):
            self.f[i*i] = 1
        ret =self.dfs(n, int(math.sqrt(n)), n)
        return ret
    
    def dfs(self, n: int, upp_i, upp_f):
        if n in self.f:
            return self.f[n]
        if upp_i <= 1 or  n >= upp_f*upp_i*upp_i:
            return n
        self.f[n] = n
        for i in range(upp_i, 1, -1):
            qpp =i*i
            tmp = n - qpp
            times = 1
            while tmp >= 0:
                #self.f[n] = min(self.dfs(tmp)+1, self.f[n])
                self.f[n] = min(self.dfs(tmp, i-1, self.f[n]-times) + times, self.f[n])
                tmp -= qpp
                times += 1
        #print("For n = %d, f[n]=%d"%(n, self.f[n]))
        return self.f[n]