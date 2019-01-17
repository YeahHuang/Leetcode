class Solution {
public:
    vector<string> letterCombinations(string digits) {
        static const vector<string> hash = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"}; //一开始忘记了static const
        int qpp;
        vector<string> ans;
        //ans.push_back("");
        for (int i=0; i<digits.size(); i++)
            if (digits[i]>='2' && digits[i]<='9'){
                int num = digits[i] - '0';
                vector<string> tmp;
                const string& candidate = hash[num];
                for (int j=0; j<ans.size();j++)
                    for (int k=0; k<candidate.size();k++)
                        tmp.push_back(ans[j] + candidate[k]);
                ans.swap(tmp);
                tmp.clear();
            }
        return ans;
    }

    
};