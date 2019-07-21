class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        q, p1, p2 = 0, len(num1)-1, len(num2)-1
        ans, carry = "",0
        #Improve1: num1 = list(num1) 然后就可以nums1.pop() 了 
        while p1>=0 and p2>=0: #也可以这里写or 后面判断 显得短一些anyway
            q = int(num1[p1]) + int(num2[p2]) + carry
            carry = q // 10 #Improve2:  carry, ramain = divmod(q, 10)
            ans = str(q % 10) + ans
            p1 -= 1
            p2 -= 1

        while p1>=0:
            q = int(num1[p1]) + carry
            carry = q // 10
            ans = str(q % 10) + ans
            p1 -= 1

        while p2>=0:
            q = int(num2[p2]) + carry
            carry = q // 10
            ans = str(q % 10) + ans
            p2 -= 1

        if carry:
            ans = '1' + ans

        return ans
        
    #Improve2:  referenced from https://leetcode.com/problems/add-strings/discuss/90449/Python%3A-7-line-and-52ms-(%2B-1-liner-for-fun)
    def addStrings(self, num1: str, num2: str) -> str:
        z = itertools.izip_longest(num1[::-1],num2[::-1], fillvalue='0')
        res, carry, zero2 =[], 0, 2*ord('0') #ord('a') = 97
        for i in z:
            cur_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
            res.append(str(cur_sum%10))
            carry = cur_sum // 10
        return ('1' if carry else '') + ''.join(res[::-1])

    def addStrings(self, num1, num2):
     return str(
              reduce(lambda a, b: 10*a + b, 
                 map(lambda x: ord(x[0])+ord(x[1])-2*ord('0'),
                   list(itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0'))[::-1]
                 ) 
              )
            )

     #这里就是觉得有空还是好好把itertools的东西学习一下 比如这里的itertools.izip_longest 还挺好的
     #https://www.programcreek.com/python/example/18445/itertools.zip_longest