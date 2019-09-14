class Solution(object):
    def minCost(self, costs: List[List[int]]) -> int:
        r, g, b = 0, 0, 0
        for cost in costs:
            r, g, b = min(g,b)+cost[0], min(r,b)+cost[1], min(r,g) + cost[2]
        return min(r,g,b)

    #Improved: 72ms -> 40ms   
    def minCost(self, costs): 
        return min(reduce(lambda (A,B,C), (a,b,c): (a+min(B,C), b+min(A,C), c+min(A,B)),
                      costs, [0]*3))
        #def reduce(function, iterable, initializer=None) 超酷对不对！ 定义初始化直接搞定了
        #但很奇怪 python2可以通过 python3即使from functools import reduce 还是一直显示语法错误 anyway先不管了吧

'''
关于functools的reduce用法：
https://www.liaoxuefeng.com/wiki/897692888725344/989703124920288

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))

map(f(1个参数)， list)
reducef(2个参数 iterate), list, initializer)