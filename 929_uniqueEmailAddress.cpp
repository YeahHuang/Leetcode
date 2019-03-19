class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        int q,p1,p2,i;
        string s;
        bool flag_at;
        unordered_map<string, bool> m;
        for (auto email: emails){
            s="";
            flag_at = false;
            for (i=0;i<email.size();i++){
                switch(email[i]){
                    case '+': while (email[++i]!='@');  s+=email.substr(i); flag_at=true;  break; 
                    case '.': break;
                    case '@': s+=email.substr(i); flag_at=true; break;
                    default:  s+=email[i]; break;
                }
                if (flag_at) break;
            }
            //if (debug) printf("email=%s, s=%s\n",email.c_str(), s.c_str());
            m[s] = true;
        }
        return m.size();
    }

private:
    bool debug=true;
};

//20ms 815.1K faster than 97.23% space less than 48.16%