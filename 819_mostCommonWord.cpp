class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_map<string, int> count;
        unordered_set<string> ban(banned.begin(), banned.end());
        
        //for (auto c: paragraph) 一定要引用才能被真的修改
        for (auto &c: paragraph)
            c = isalpha(c)?tolower(c):' ';
        
        istringstream iss(paragraph);
        pair<string, int> res("",0);
        string w; //一定要申明 才能用 
        //for (iss>>w){ //是for 
        while (iss>>w){
            if (ban.find(w)==ban.end() && ++count[w] > res.second)
                res = make_pair(w, count[w]);
        }
        
        return res.first;
        
    }
};