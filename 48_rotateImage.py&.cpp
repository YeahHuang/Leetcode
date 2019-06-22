//C++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int q, p1, p2, i, j, n = matrix.size();//[[1]] 一定要考虑全 size=0 size=1 size=奇数/偶数的情况
        p1 = p2 = (n-1)/2;
        if (n%2) p2 -= 1;  // += vs -=
        for (int i=0; i<=p1; i++) //< vs <=
            for (int j=0; j<=p2; j++){
                swap(matrix[i][j], matrix[j][n-1-i]);
                swap(matrix[i][j], matrix[n-1-i][n-1-j]);
                swap(matrix[i][j], matrix[n-1-j][i]);
            }
        //return matrix;     一开始写了return 要记住返回值是void哦
    }
};


#Python


class Solution:
    def rotate(self, matrix):

        #Sol 1 44ms  pythonic but not accepatble sometimes
        matrix[:] = zip(*matrix[::-1])     #[::-1]可以upside down A   然后zip transpose一下

        #Sol 2 56ms 不再是tuple是list了
        matrix[:] = map(list, zip(*matrix[::-1]))

        #Sol3 60ms 用list代替zip
        matrix[:] = [[row[i]] for row in matrix[::-1] for i in range(len(matrix))]

        #Sol4 52ms 直接in-place. 用[~i]表示了[n-1-i]
        n = len(matrix)
        for i in range(n//2):
            for j in range(n-n//2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                            matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]