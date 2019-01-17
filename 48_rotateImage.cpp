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