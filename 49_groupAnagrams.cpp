class Solution {
public:
    int prime[26] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101};//一开始这个放在函数里了。没有注意变量的作用域问题； 一开始写成了[] list初始化需要用{}哦！
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        int qpp, n = strs.size();
        unordered_map<int, vector<string>>  hash;
        for (int i=0; i<n; i++)
            hash[str2int(strs[i])].push_back(strs[i]);
        for (auto& e : hash)
            ans.push_back(e.second);
        return ans;
    }
private:
    int str2int(string str){
        int ret = 1;  //没有写判断是否会超过INT_MAX 所以其实是不安全的
        for (int i=0; i<str.size();i++)
            ret *= prime[str[i]-'a'];
        return ret;
    }
};


//faster than 79.6%