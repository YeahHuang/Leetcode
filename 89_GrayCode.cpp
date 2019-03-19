class Solution {
public:
    vector<int> grayCode(int n) {//0ms
        int q,p1,p2;
        vector<int>  er;
        vector<int> ret;
        for (int i=0; i<=n; i++)
            er.push_back(1<<i);
        vector<bool> hasExist(er[n], false);
        ret.push_back(0);
        q = 0;
        hasExist[0]=true;//一开始这个忘写了  要好好初始化！
        for (int i=1; i<er[n];i++)
        {
            for (int j=0;j<n; j++){
                p1 = (q&er[j]) ? (q-er[j]):(q+er[j]);
                if (!hasExist[p1]) {
                    if (debug) printf("j=%d,p1=%d ",j,p1);
                    break;
                }
            }
            ret.push_back(p1);
            hasExist[p1] = true;
            q = p1;
        }
        return ret;//一开始这个忘写了 要记得返回吖！
    }

private:
    bool debug = true;
    
};