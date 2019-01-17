class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int qpp, m,n, col0=1;
        m = matrix.size();
        if (m>0)
        {
            n = matrix[0].size();
            if (n>0)
            {
                for (int i=0; i<m; i++){
                    if (matrix[i][0]==0) 
                        col0 = 0;
                    for (int j=1; j<n; j++) //一开始写j=0；开始 果断哇了
                        if (matrix[i][j]==0){
                            matrix[i][0] = 0;
                            matrix[0][j] = 0;                    
                        }
                    };
                for (int i=1; i<m; i++)
                    for (int j=1; j<n; j++)
                        if (matrix[i][0]==0 ||  matrix[0][j]==0)//一开始自作聪明的写了(matrix[i][0] * matrix[0][j]==0) 忽略了c++的范围问题
                            matrix[i][j] = 0;
                if (matrix[0][0]==0)
                    for (int j = 1; j<n; j++) 
                        matrix[0][j] = 0;
                if (col0==0)
                    for (int i = 0; i<m; i++)
                        matrix[i][0] = 0;
            }      
        }
        

    }
};

//本来想说把所有的设置成一个 >max 的值。 然后最后再全部复原 这样就意味着需要 num(0) * 2n + n 

//永远不要小看任何一道题emmm 我看了别人的代码 急于求成的希望ok。 结果wa了两次才AC emmm 加油～
