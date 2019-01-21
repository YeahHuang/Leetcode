class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> ans;
        for (int i=0; i<nums.size();i++){ //一开始写成了i<num.size() 关于nums写成num的bug 我好像犯了很多次了
            if (!dq.empty() && dq.front()==i-k)  
                dq.pop_front();
            //这里很巧妙。 我一开始也想到了类似的插入排序。  但是一直卡在如何定位要删除的元素 想到了hashmap，但还是要查找。in/out。 
            //这里它说只需要它是max 才check index。 只要是末尾的，都会入队并淘汰比他小的。逻辑666 懂了逻辑后1次AK。
            while (!dq.empty() && nums[i]>=nums[dq.back()])  
                dq.pop_back();
            dq.push_back(i);
            if (i+1>=k) ans.push_back(nums[dq.front()]);
        }
        return ans;
    }
};

