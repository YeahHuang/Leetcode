class Solution {
public:
    vector<int> rightSideView(TreeNode* root) { //4ms faster than 98.59%
        preTraverse(root, 0);
        vector<int> rightV;
        for (auto v0: v)
            rightV.push_back(v0.back()); //一开始这里写成了v.back() 谨慎谨慎谨慎吖
        return rightV;
    }


private:
    vector<vector<int>> v;
    void preTraverse(TreeNode* root, int depth){
        if (root){
            if (v.size()==depth) v.push_back(vector<int>());
            v[depth].push_back(root->val);
            preTraverse(root->left, depth+1);
            preTraverse(root->right, depth+1);
        }
    }
};

Bmwanm960907