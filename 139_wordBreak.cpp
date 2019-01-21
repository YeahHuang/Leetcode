class Solution {
public:
    bool debug = true;
    /*
    bool wordBreak(string s, vector<string>& wordDict) { //因为没有判断范围，导致了空string指针，RTL了2次
        bool ans = false;
        int length_word, length_s = s.size();
        if (s.empty()) ans = true;
        else
        for (auto word : wordDict){
            length_word = word.size();
            //if (length_s>length_word && strncmp(s.c_str(), word.c_str(), length_word) && (length_word == length_s || wordBreak(s.substr(length_word), wordDict)))
            if (debug) cout<<s<<','<<word<<endl;
            if (length_s>=length_word && s.substr(0, length_word).compare(word)==0 && (length_word==length_s || wordBreak(s.substr(length_word), wordDict)))
            {
                ans = true;
                break;
            }
        }
        return ans;
    }*/
    bool wordBreak(string s, vector<string>& wordDict) {
        int qpp, num_words, n = s.size();
        num_words = wordDict.size();
        vector<bool> flag_break(n,false); //represents end with s[i] true/false  abcded ab cde i = 4 j=2 len_j = 3 
        if (num_words){ //WA3 极致判断。 题目中提到了2个non-empty（ non-empty string s + a list of non-empty words) 可是没说lists是non-empty呀！
            vector<int> length_word(num_words,0);
            compare c;
            sort(wordDict.begin(), wordDict.end(),c);
            for (int i=0; i<num_words; i++){
                length_word[i] = wordDict[i].size();
                if (length_word[i]>n) break;
                if (s.substr(0, length_word[i]).compare(wordDict[i])==0) //WA0 一开始忘记判断了，而是直接长度相等 就直接=true
                    flag_break[length_word[i]-1]=true; //WA1 Index ERROR 忘记-1 index都是length-1哦～
            }
            if (debug) cout<<wordDict[0]<<endl;
            for (int i=wordDict[0].size(); i<n; i++) //WA2 Index ERROR  一开始写成i=wordDict[0].size()+1
                for (int j=0;j<num_words;j++){
                    if (i+1<=length_word[j]) break;  
                    if (flag_break[i-length_word[j]] && s.substr(i-length_word[j]+1, length_word[j]).compare(wordDict[j])==0){
                        flag_break[i] = true;
                        break;
                    }
                }
        }
        return flag_break[n-1];
    }
private:
    struct compare { //学习！ compare + substr + compare http://www.cplusplus.com/reference/string/string/substr/
        bool operator()(const std::string& first, const std::string& second) {
            return first.size() < second.size();
        }
    };
};

//直接暴力会超时。DP 4ms >88.65%