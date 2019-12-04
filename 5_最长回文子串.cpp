
//56ms faster than 47.96%
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

//48ms
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        int q,p1,p2, ans = 1;
        int n = s.length();
        string ret = s.substr(0,1);
        for (int i=1; i<n; i++){
            p1 = expand(s, n, i-1, i);
            if (p1>ans)
            {
                ans = p1; ret = s.substr(i-p1/2,p1 );
            }
            if (i!=n-1) {
                p2 = expand(s, n, i-1, i+1);
                if (p2>ans)
                {
                    ans = p2; ret = s.substr(i-p2/2,p2 );
                };
            };
        };
        return ret;
    }
private:
    int expand(string s, int n, int left, int right){
        if (s[left]!=s[right])
            return 0;
        while (left-1>=0 && right+1<n && s[left-1]==s[right+1])
            {left--;right++;};
        return right-left+1;
    }
};

//dp
class Solution {
public:
    // dp: palin[i][j] = (s[i]==s[j] && s[i+1][j-1])
    // substr -> make_pair 1556ms -> 184ms
    string longestPalindrome(string s) {
        bool palin[1001][1001];
        int n = s.size();
        if (n==0) return "";
        //string res = s.substr(0,1); //s.substr(start_idx, len)
        pair<int, int> res = {0,1};
        for (int i=0; i<n-1; i++){
            palin[i][i] = true;
            palin[i][i+1] = (s[i]==s[i+1]);
            if (palin[i][i+1])
                //res = s.substr(i,2); 
                res = make_pair(i, 2);
        }
        palin[n-1][n-1] = true;
        for (int len=2; len < n; len++)
            for (int i=0; i < n-len; i++){ // i + len < n  so i < n-len
                if (s[i] == s[i+len] && palin[i+1][i+len-1]){
                    //res = s.substr(i, len+1);
                    res = make_pair(i, len+1);
                    palin[i][i+len] = true;
                }
                else palin[i][i+len] = false;
            }
        //return res;
        return s.substr(res.first, res.second);
    }
};