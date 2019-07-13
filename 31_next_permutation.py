class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in range(len(nums)-1, 0, -1):
            if nums[i]>nums[i-1]:
                cur_min, idx = float("inf"), -1     
                for j in range(i, len(nums)): 
                    if nums[j]>nums[i-1] and nums[j]<cur_min:
                        cur_min = nums[j]
                        idx = j
                if idx == -1:
                    break
                nums[i-1], nums[idx] = nums[idx],nums[i-1]
                #nums[i:] = sorted(nums[i:])
                nums[i:] = nums[]
                flag = True
                break
        if flag==False:
            nums.sort() #其实直接nums.reverse() 即可吖 因为已经max

        #改进版 但不知道为啥reverse 和 sort速度一点没快啊 reverse 44ms&40ms. sort 40ms

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in range(len(nums)-1, 0, -1):
            if nums[i]>nums[i-1]:
                cur_min, idx = float("inf"), -1     
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        idx =j
                        break
                    
                if idx == -1:
                    break
                nums[i-1], nums[idx] = nums[idx],nums[i-1]
                #nums[i:] = sorted(nums[i:]) 44ms
                nums[i:] = reversed(nums[i:]) #49ms
                flag = True
                break
        if flag==False:
            nums.reverse()
        
        '''
        c++自带的：
        void nextPermutation(vector<int>& nums) {
            next_permutation(begin(nums), end(nums));
        }

        class Solution { plus 降序加成 就可以KO啦
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size(), k, l;
        for (k = n - 2; k >= 0; k--) {
            if (nums[k] < nums[k + 1]) {
                break;
            }
        }
        if (k < 0) {
            reverse(nums.begin(), nums.end());
        } else {
            for (l = n - 1; l > k; l--) {
                if (nums[l] > nums[k]) {
                    break;
                }
            } 
            swap(nums[k], nums[l]);
            reverse(nums.begin() + k + 1, nums.end());
        }
    }
}; 
        '''
