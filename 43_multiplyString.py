class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mul = [0 for i in range(len(num1)+len(num2))]
        n1 = [ord(c)-ord('0') for c in num1[::-1]]
        n2 = [ord(c)-ord('0') for c in num2[::-1]]
        for i, p1 in enumerate(n1):
            for j, p2 in enumerate(n2):
                mul[i+j] += p1 * p2
        ans = ""
        for i in range(len(mul)-1):   
            mul[i+1] += mul[i] // 10
            mul[i] %= 10
        while len(mul)>1 and mul[-1]==0:
            mul.pop()
 
        #⬇️这三行可以直接写成：  return ''.join(map(str, mul[::-1]))
        for i in range(len(mul)-1, -1, -1):
            ans += str(mul[i])
        return ans
        

        
'''补充一下map的用法：
>>>def square(x) :            # 计算平方数
...     return x ** 2
... 
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
 
# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]
'''