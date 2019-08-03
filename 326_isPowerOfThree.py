class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        Sol1: recursion
        Sol2: java里转换成三进制 python不可行
        Sol3: math.log 判断 log3(n）是否为整数 
        虽然python有sys.float_info.epsilon 来表示 但是我觉得还是不要这样考验float更好
        Sol4: 其实对于python不算很好 但能pass全部的test case
        '''
        return n and (3**19)%n==0 