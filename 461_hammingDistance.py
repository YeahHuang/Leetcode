class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        qpp = x ^ y 
        dist = 0
        while qpp > 0:
            dist += qpp & 1
            qpp = qpp >> 1 #qpp >>= 1 是不存在的表达哈
        return dist