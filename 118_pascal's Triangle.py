class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows-=1
        if numRows==0:
            return [[1]]
        if numRows==-1:#没判断空 WA一次
            return []
        rows=[[1],[1,1]]
        for i in range(2,numRows+1):               
            rows.append([1] * (i+1))
            for j in range(1,i):
                rows[i][j] = rows[i-1][j-1]+rows[i-1][j]
        return rows