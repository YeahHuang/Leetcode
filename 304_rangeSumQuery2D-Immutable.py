class NumMatrix(object):#就是纯dp还是需要一些分析的 这里也可以从1开始标号 就省的每一个都判断了

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        #in-place:
        for i, row in enumerate(matrix):
            for j in range(len(row)):
                matrix[i][j] += (matrix[i-1][j] if i else 0) + (matrix[i][j-1] if j else 0) - (matrix[i-1][j-1] if i*j else 0)
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        return self.matrix[row2][col2] - (self.matrix[row2][col1-1] if col1 else 0) \
        - (self.matrix[row1-1][col2] if row1 else 0)  + (self.matrix[row1-1][col1-1] if row1*col1 else 0)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)