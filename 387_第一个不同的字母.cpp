class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> hash;
        int qpp = -1;
        for (char c='a';c<='z';c++)
            hash[c] = 0;
        for (auto c: s)
            hash[c]+=1;  //一开始写成了unordered_map[c]
        for (int i=0; i<s.size();i++)
            if (hash[s[i]]==1) {qpp =i; break;}
        return qpp;
    }
};