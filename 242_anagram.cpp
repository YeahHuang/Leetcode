class Solution {
public:
    /*
    bool isAnagram(string s, string t) { //12ms
        int q,p1,p2;
        bool flagAnagram = true;
        unordered_map<char, int> m;
        if (s.length()!=t.length()) flagAnagram = false;
        else{
            for (char c:s)  // c++的unordered_map和python的dict不一样. 它会自动创建+初始化int为0 按照我没注释的是20ms 现在是12ms
                //if (m.find(c)==m.end()) m[c]=1; else 
                m[c]+=1;
            for (char c:t)
                //if (m.find(c)==m.end()) {if (debug) printf("t don't have %c\n",c); flagAnagram=false;break;}else 
                m[c]-=1;
            if (flagAnagram)
                for (auto it=m.begin(); it!=m.end(); it++)
                    if (it->second!=0) {if (debug) printf("m[%c] = %d\n", it->first, it->second);flagAnagram=false;break;};
        }
        return flagAnagram;     
    }*/


    bool isAnagram(string s, string t){ //4ms 因为array比unordered_map快多了
        int q,p1,p2,n;
        bool flagAnagram=true;
        int counts[26]={0};
        if (s.length()!=t.length()) flagAnagram = false;
        else {
            n = s.length();
            for (int i=0; i<n; i++)
            {
                counts[s[i]-'a']++;
                counts[t[i]-'a']--;//一开始这里也写成了++ 自然是错的了
            }
            for (int i=0; i<26;i++)
                if (counts[i]) {flagAnagram=false; break;};
        }
        return flagAnagram;
    }
private:
    bool debug;
};