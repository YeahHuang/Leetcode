class Solution {
public:
    /*int numJewelsInStones(string J, string S) { 8ms
        unordered_map<char, bool> hash;
        int ret = 0;
        for (char c: J) hash[c]=true;
        for (char c: S) 
            if (hash.find(c)!=hash.end())
                ret++;
        return ret;
    }*/
    
    int numJewelsInStones(string J, string S) { //also 8ms  可以学一下unordered_set的用法～
        int res = 0;
        unordered_set<char> setJ(J.begin(), J.end());
        for (char s : S) if (setJ.count(s)) res++;
        return res;
    }
};