class Solution:
    def countBits(self, num: int) -> List[int]:
        ret = [0] * (num+1) #碰到bits不要怕 慢慢去思考其中的细节就好
        cur = [0] * (len(bin(num))-2)
        for i in range(num):
            j = 0
            while cur[j]==1:
                cur[j] = 0
                j += 1
            cur[j] = 1
            ret[i+1] = ret[i] + 1 - j 
        return ret
            
            
            