/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:

    vector<vector<int>> levelOrder(TreeNode* root){ //4ms fastr than 99.83%
        preTraverse(root, 0);
        return v;
    }

    void preTraverse(TreeNode* root, int depth){
        if (root){
            if (v.size()==depth) v.push_back(vector<int>());
            v[depth].push_back(root->val);
            preTraverse(root->left, depth+1);
            preTraverse(root->right, depth+1);
        }
    }

    /*vector<vector<int>> levelOrder(TreeNode* root) { //这样到depth=762的时候 就会RE 
        int q,p1,p2;
        int depth = getDepth(root);
        vector<int> v(1<<depth,-1);//一开始写1<<depth-1 实际执行顺序是1<<depth - 1
        if (debug) printf("depth=%d, v.size()=%d\n", depth,v.size());
        tree2vec(root, v, 0);
        //vector<int> v = tree2vec(root);
        vector<vector<int>> ret;
        int level;
        level = 0;
        vector<int> er(depth+1,0);
        for (int i=1; i<=depth; i++) er[i] = er[i-1]*2 + 1;
        while (level < depth){
            vector<int> qpp;
            //if (1<<(level+1)-1> v.size()) printf("ERROR!1<<(level+1)-1 =%d v.size()=%d\n",1<<(level+1)-1,v.size());
            for (int i=er[level]; i<er[level+1];i++){
                if (v[i]!=(-1)) qpp.push_back(v[i]); 
            }
            if (!qpp.empty()) ret.push_back(qpp);
            level++; //一开始忘记这一行了 导致死循环超时
        }
        return ret;
    }

    void tree2vec(TreeNode* root, vector<int>& v, int idx){
        if (idx>=v.size()) {printf("ERROR! idx=%d, v.size()=%d.", idx, v.size()); }
        else
        if (root){
            v[idx] = root->val;
            if (debug) printf("v[%d]=%d\n",idx, root->val);
            if (root->left) tree2vec(root->left, v, idx*2+1);
            if (root->right) tree2vec(root->right, v, idx*2+2);
        }
    }
    
    vector<int> tree2vec(TreeNode* root){ //一开始这个写法针对[3,9,20,null,null,15,7] v.size()会得到11
        vector<int> ret;
        if (root) {
            vector<int> left = tree2vec(root->left vector<vector<int>>& );
            vector<int> right = tree2vec(root->right);
            left.push_back(root->val);
            if (root->val==-1) printf("ERROR!root->val=-1\n");
            left.insert(left.end(), right.begin(), right.end());
            ret = left;
        }   
        else ret.emplace_back(-1);
        return ret;
    }*/

private:
    bool debug = true;

    vector<vector<int>> v;
    int getDepth(TreeNode* root){
        int depth;
        if (!root) depth = 0;
        else if (!(root->left) && !(root->right)) depth = 1; //WA1 一开始写成了!root->left
                                         else  depth = max(getDepth(root->left), getDepth(root->right)) + 1;
        return depth;
    }
};