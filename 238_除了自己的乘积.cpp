class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int qpp, left, right, n = nums.size();
        vector<int> product(n,0);
        left = 1;
        right = 1;
        for (int i=0;i<n;i++){
            product[i] = left;
            left *= nums[i];
        }
        for (int i=n-1;i>=0;i--){
            product[i] *= right;
            right *= nums[i];
        }
        return product;

    }
};//56ms 23.32%