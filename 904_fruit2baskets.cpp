class Solution {
public:
    int totalFruit(vector<int>& tree) {
        int q,p1,p2,ret, n, i;
        n = tree.size();
        i = 0;
        ret = 0;
        tree.push_back(-1);// in case out of range
        while (i<n){
            p1 = tree[i];
            while (i<n && tree[++i]==p1); // can be changed into while (tree[++i]==p1);
            if (debug) printf("p1=%d, i=%d, tree[i]=%d\n",p1,i, tree[i]);
            if (i<n){
                
            }
        }

        return ret;
    }
};

// 1 2 1 totally skip.    1 2 start from 2 