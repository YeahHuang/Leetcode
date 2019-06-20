class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        m = {}
        '''                             #都是32ms 14.7M
        for i in range(len(nums)):
            if nums[i] in m:
                return [m[nums[i]], i]
            else:
                m[target - nums[i]] = i
        '''
        
        for i, num in enumerate(nums):
            if num in m:
                return [m[num], i]
            else:
                m[target - num] = i


class Solution {        //8ms 1.8M c++果然是🐂🍺 
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i,j,n;
        vector<int> ans;
        unordered_map<int,int> m;
        n = nums.size();
        for (i=0;i<n;i++)
            if (m.find(nums[i])==m.end())
            {
                m[target-nums[i]]=i;
            }else
            {
                ans.push_back(m[nums[i]]);
                ans.push_back(i);
                return ans;
            }
    }
};