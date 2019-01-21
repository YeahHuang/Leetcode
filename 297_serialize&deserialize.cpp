/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec { // 1/2.\3/4.\5.
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string ret;
        if (root==nullptr) ret = '#';
        else ret = to_string(root->val) + "," + serialize(root->left) + "," + serialize(root->right);
        return ret;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        return mydeserialize(data);
    }

private:
    bool debug = true; 
    TreeNode* mydeserialize(string& data) {
        bool flag_null = false; //一开始就是这里为了一个出口，然后一直是空！ 看来nullptr是一个神奇的一定要直接用的东西！ 不能node=nullptr
        TreeNode* node;
        if (data[0]=='#'){
            if (data.size()>1) data = data.substr(2); //还有逗号
            flag_null = true;
        } else {
            node = new TreeNode(helper(data));
            node->left = mydeserialize(data);
            node->right = mydeserialize(data);
            //return node;
        }
        return flag_null?nullptr:node;
    }
    
    int helper(string& data){
        int ret;
        int pos = data.find(",");
        ret = stoi(data.substr(0,pos));
        data = data.substr(pos+1);
        if (debug) printf("In helper ret=%d\n",ret);
        return ret;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));

/*In interview setting, it's perfectly reasonable to assume hash table add/delete operations are O(1). Unless you are explicitly asked about the detailed implementation of a hash table, then you should mention that in real world, hash table could degrade to O(n) due to collision (though unlikely if you choose a good hashing algorithm).

Hash table is seen as a basic building block and is used so often to build efficient solution to interview problems. Without assuming the mentioned operations are O(1), most problems which could be solved in hash table efficiently will have the same complexity of brute force approaches.*/