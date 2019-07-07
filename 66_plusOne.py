class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        jinwei = 1
        #jinwei = ( digits[len(digits)-1] + 1 ) / 10
        #digits[len(digits)-1]  = (digits[len(digits)-1] + 1)%10
        #长度为0 长度为1 长度+1
        for i in range(len(digits)-1, -1 , -1):
            if jinwei==0:
                break
            jinwei = (digits[i] + 1) // 10 #WA一次 注意python3的div是//
            digits[i] = (digits[i] + 1) % 10 #WA一次 殊不知jinwei是会被改变的 一开始写成了digits[i] = (digits[i] + jinwei) % 10 
        if jinwei:
            digits = [1] + digits
        return digits