class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Sol1 但两个都是80ms 大概因为强大的bisect！！
        #没看清题目 明明是全部sort
        if len(matrix) and len(matrix[0]):
            for row in matrix:
                if row[0]<=target<=row[-1]:
                    qpp = bisect.bisect_left(row, target)
                    if qpp < len(row) and row[qpp] == target:
                        return True
        return False
        '''
        if len(matrix) and len(matrix[0]):
            m, n = len(matrix), len(matrix[0])
            l, r = 0, m*n-1
            while (l<=r):
                mid = (l+r) >> 1
                if matrix[mid//n][mid%n] == target:
                    return True
                if matrix[mid//n][mid%n] < target:
                    l = mid + 1 #WA 一次 还怎么也看不出来 后来发现写反了！
                else:
                    r = mid - 1
        return False
    
      