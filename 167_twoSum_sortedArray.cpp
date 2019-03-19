class Solution{
public:
    vector<int> twoSum(vector<int>& numbers, int target){ //4ms >99.08%
        int q,p1,p2,l, r;
        vector<int> ret;
        l = 0;
        r = numbers.size()-1;
        while (l<r){
            q = target-numbers[l];
            while (l<r && numbers[r]>q) r--;
            if (l<r && numbers[r]==q) {
                ret.push_back(l+1);//明明题目中强调了不是0-index 这里一开始还是写错了 
                ret.push_back(r+1);
                break;
            }
            l++;
        }
        return ret;
    }
}; //一开始因为没有加封号 CE一次

