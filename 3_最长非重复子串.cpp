#include <unordered_map>
#include <iostream> 
#include <vector>

using std::unordered_map;
using std::vector;

class Solution { //faster than 26.99%
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> lastPos;  //vector<int> dict(256, -1);
        int maxLength = 0, curLength = 0;
        for (int i = 0; i<s.length(); i++){  //一开始忘记了s.length()
            if ((lastPos.find(s[i])!=lastPos.end()) && (i-lastPos[s[i]] <= curLength)) //c++不是 s[i] in lastPos.keys; <与<=也错了一次
               curLength = i - lastPos;
            else
               curLength += 1;
            lastPos[s[i]] = i;
            maxLength = maxLength > curLength ? maxLength : curLength;
        }
    return maxLength;

    }
};

/*
int lengthOfLongestSubstring(string s) {
        vector<int> dict(256, -1);
        int maxLen = 0, start = -1;
        for (int i = 0; i != s.length(); i++) {
            if (dict[s[i]] > start)
                start = dict[s[i]];
            dict[s[i]] = i;
            maxLen = max(maxLen, i - start);
        }
        return maxLen;
    }
*/