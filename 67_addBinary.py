class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            a, b = b, a
        ia = len(a) - 1
        ib = len(b) - 1
        add = "" 
        carry = 0 
        while ia >= 0:
            add = str((int(a[ia])+int(b[ib])+carry)%2) + add #一开始错误的写成a[ia]-'0' 这个是c++ python需要int转换哦 
            carry = (int(a[ia])+int(b[ib])+carry) // 2  #一开始还忘记了str()
            ia, ib = ia-1, ib-1
        while ib >= 0:
            add = str((int(b[ib])+carry)%2) + add #carry, rem = divmod(int(a[ia])+int(b[ib])+carry, 2)
            carry = (int(b[ib])+carry) // 2
            ib -= 1
        if carry == 1:
            add = '1' + add
        return add

