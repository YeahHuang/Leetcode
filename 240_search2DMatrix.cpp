class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        bool ret = false;
        targ = target;
        mat = matrix;
        if (matrix.size() && matrix[0].size())
            //ret = mySearchMatrix(0, 0,matrix.size(), matrix[0].size());
            ret = mySearchMatrix1(matrix, 0,0, matrix.size(), matrix[0].size(), target);
        return ret;
    }

private:
    bool debug = true; 
    vector<vector<int>> mat;
    int targ;
    bool mySearchMatrix1(vector<vector<int>>& matrix, int x, int y, int m, int n, int target){
        int x1,y1;
        bool ret=false;
        if (m && n && target>=matrix[x][y] && target<=matrix[x+m-1][y+n-1] )
        if (m+n<=4) {
            for (int i=x; i<x+m; i++)
                for (int j=y; j<y+n; j++)
                    if (matrix[i][j]==target) ret = true;
        } else{
            if (m>n) { 
                x1 = x + m/2; y1 = y+n-1;
                if (matrix[x1][y1] == target) ret=true;
                    else ret = (matrix[x1][y1] > target)? mySearchMatrix1(matrix, x, y, m/2+1, n,target): mySearchMatrix1(matrix, x1+1, y, m/2, n, target);
            }   
            else { 
                x1 = x+m-1; y1 = y + n/2;
                if (matrix[x1][y1] == target) ret=true;
                    else ret = (matrix[x1][y1] > target)? mySearchMatrix1(matrix, x, y, m, n/2+1, target): mySearchMatrix1(matrix, x, y1+1, m, n/2, target);
            };
        }

        
        
        return ret;
    }

/*runtime error: reference binding to misaligned address 0x33383137353736f9 for type 'value_type', which requires 4 byte alignment (stl_vector.h)
0x33383137353736f9: note: pointer points here
<memory cannot be printed>*/
    bool mySearchMatrix(int x, int y, int m, int n){
        int x1,y1;
        bool ret=false;
        if (m && n && targ>=mat[x][y] && targ<=mat[x+m-1][y+n-1] )
        if (m+n<=4) {
            for (int i=x; i<x+m; i++)
                for (int j=y; j<y+n; j++)
                    if (mat[i][j]==targ) ret = true;
        } else{
            if (m>n) { 
                x1 = x + m/2; y1 = y+n-1;
                if (debug) printf("x=%d y=%d m=%d n=%d x1=%d y1=%d mat[x1][y1]=%d\n", x, y, m,n, x1, y1, mat[x1][y1]); //不要和python的print搞混了！ 一开始写成了printf("x=%d y=%d m=%d n=%d x1=%d y1=%d mat[x1][y1]=%d\n"%(x, y, m,n, x1, y1, mat[x1][y1]));                
                    if (mat[x1][y1] == targ) ret=true;
                    else ret = (mat[x1][y1] > targ)? mySearchMatrix(x, y, m/2+1, n): mySearchMatrix(x1+1, y, m/2-1, n);
            }   
            else { 
                x1 = x+m-1; y1 = y + n/2;
                if (debug) printf("x=%d y=%d m=%d n=%d x1=%d y1=%d mat[x1][y1]=%d\n",x, y, m,n, x1, y1, mat[x1][y1]);
                if (mat[x1][y1] == targ) ret=true;
                    else ret = (mat[x1][y1] > targ)? mySearchMatrix(x, y, m, n/2+1): mySearchMatrix( x, y1+1, m, n/2-1); //一开始(y+n-1) -  (y+n/2+1) +1 算成了n/2+1
            };
        }

        
        return ret;
    }
};