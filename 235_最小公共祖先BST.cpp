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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* ancester=NULL;
        if (root==NULL || p==NULL || q==NULL) printf("ERROR! null\n ");
        else
        {
            if ((p->val - root->val) * (q->val - root->val) <=0)  ancester = root;
        else if (p->val < root->val) ancester = lowestCommonAncestor(root->left, p, q);
            else ancester = lowestCommonAncestor(root->right, p, q);
        }
        
        return ancester;
    }
};