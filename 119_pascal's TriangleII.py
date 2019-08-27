class Solution:
    def getRow(self, idx):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if idx==0:
            return [1]
        prev = [1,1]
        for i in range(2,idx+1):               
            cur = [1] * (i+1)
            for j in range(1,i):
                cur[j] = prev[j] + prev[j-1]
            prev = cur
        return prev