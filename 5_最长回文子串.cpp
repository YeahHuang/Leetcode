class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return ""; //极值忘记考虑
        if (s.length() == 1) return s;
        int validLength[1005][1005],maxLength = 1, startIdx=0, j,k; //一开始忘记声明j,k startIdx=0 忘记说了
        validLength[0][0] = 1;
        validLength[0][1] = 0;
        string ans;
        for (int i=1; i<s.length(); i++){
            j=0;
            k=0;
            validLength[i][k] = 1;
            k++;
            if (s[i]==s[i-1]) {
                validLength[i][k] = 2;
                k++;
            }
            while (validLength[i-1][j]!=0){
                if (i - validLength[i-1][j] - 1 >=0 and s[i - validLength[i-1][j] - 1] == s[i]){
                    validLength[i][k] = validLength[i-1][j] + 2;
                    k++;
                }
                j++;
            }
            validLength[i][k] = 0; // c++并不会自动初始化，所以提交时导致出错
            if (validLength[i][k-1]>maxLength){
                maxLength = validLength[i][k-1];
                startIdx = i - maxLength + 1;
            } 
        };
        return s.substr(startIdx, maxLength);
    }
};

//faster than 47.96%