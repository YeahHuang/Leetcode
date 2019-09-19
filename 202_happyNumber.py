class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        exist = set([n])
        while True:
            n =  sum(map(lambda x: int(x)**2, list(str(n)))) 
            #n = sum([int(i)**2 for i in str(n)]) 也可以这样写 都是40ms
            if n == 1:
                return True
            if n in exist:
                return False
            else:
                exist.add(n)
        return False