//stable: bubble & merge
//unstable: heap & quicksort
// ps c的if后要有括号 然后class的}后要有分号
//referenced from @lzl1234631x
using namespace std;
//Sol1 20ms
bool myCompare(string a, string b){
    int i = a.find(' ');
    int j = b.find(' ');
    if (!isdigit(a[i+1]) && !isdigit(b[j+1]))
        if (a.substr(i+1) == b.substr(j+1))
            return a.substr(0,i+1) < b.substr(0,j+1);
        else
            return a.substr(i+1) < b.substr(j+1);
    else{
        if (!isdigit(a[i+1])) return true;
        return false;
    }
}
class Solution{
public:
    vector<string> reorderLogFiles(vector<string>& logs){
        stable_sort(logs.begin(), logs.end(), myCompare);
        return logs;
    };
};

//Sol2 12ms 确实比python的44ms快多了吖

class Solution{
public:
    vector<string> reorderLogFiles(vector<string>& logs){
        vector<string> digitLogs, ans;
        vector<pair<string, string>> letterLogs;
        for (string &s: logs){
            int i=0;
            while (s[i]!=' ') ++i;
            if (isalpha(s[i+1])) letterLogs.emplace_back(s.substr(0,i), s.substr(i+1));
            //这样不对if (isalpha(s[i+1])) letterLogs.push_back(s.substr(i+1) + " "+s.substr(0,i));
            else digitLogs.push_back(s);
        }
        sort(letterLogs.begin(), letterLogs.end(), [&](auto& a, auto& b){
            return a.second == b.second ? a.first < b.first: a.second < b.second;
        });
        for (auto &p: letterLogs) ans.push_back(p.first + " " + p.second);
        for (string &s: digitLogs) ans.push_back(s);
        return ans;
    }
};