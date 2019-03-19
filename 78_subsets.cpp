class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        n = nums.size();
        dfs(nums,0, vector<int>());
        return set;
    }
    
private:
    vector<vector<int>> set;
    int n;
    void dfs(vector<int>& nums, int step, vector<int> subset){
        if (step==n){
            set.push_back(subset);
        } else{
            dfs(nums, step+1, subset);
            subset.push_back(nums[step]);
            dfs(nums, step+1, subset);
        }
    }
};

//4ms 一次AK faster than 100%s