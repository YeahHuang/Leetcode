class Solution:
    def getSum(self, a: int, b: int) -> int:
        summ = ""
        sa, sb = bin(a)[2:], bin(b)[2:]
        if len(sa)>len(sb):
            sa, sb = sb, sa
        ia, ib = len(sa)-1, len(sb)-1
        carry = 1
        while ia>=0 and ib>=0:
            if carry==1:
                if sa[ia]=='1' and sb[ib]=='1':#3个1
                    carry = 1
                    summ = '1' + summ
                elif sa[ia] =='1' or sb[ib] == '1':#2个1
                    carry = 1
                    summ = '0' + summ
                else:               #1个1
                    carry = 0
                    summ = '1' + summ
            else:
                if sa[ia]=='1' and sb[ib]=='1':#2个1
                    carry = 1
                    summ = '0' + summ
                elif sa[ia] =='1' or sb[ib] == '1':#1个1
                    carry = 0
                    summ = '1' + summ
                else:               #0个1
                    carry = 0
                    summ = '0' + summ
            ia, ib = ia-1, ib-1
        while ib>=0:
            if carry==1 and sb[ib]=='1':
                carry = 1
                summ = '0' + summ
            elif carry == 1 or sb[ib]=='1':
                carry = 0
                summ = '1' + summ
            else:
                carry = 0
                summ = '0' + summ
        if carry==1:
            summ = '1' +summ
        return int(summ, 2)

    #正负都可以 注意a是负数的时候 先把正的弄出来再取反
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            # carry = (a&b) << 1 这个可以学一下
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask) #负数的时候就需要用到else啦