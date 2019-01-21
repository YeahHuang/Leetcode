class Solution {//https://segmentfault.com/a/1190000008322873?utm_source=tuicool&utm_medium=referral
public:
    int findKthLargest(vector<int>& nums, int k) {
        if (k>nums.size()) printf("ERROR! k=%d, nums.size()=%d\n", k, nums.size());
        return BFPRT(nums, 0, nums.size()-1, nums.size()-k+1 );  
    }

private:
    bool debug = false;
    int BFPRT(vector<int>& nums, int left, int right, int k){ //note that its [left, right] both included 
        int qpp, ret=-1;
        if (debug) {
            for (int i=left; i<=right;i++) printf("%d ",nums[i]);
            printf("In BFPRT left=%d, right=%d, k=%d \n",left, right, k);
        }
        if (left>right || k<=0 || k>right-left+1) printf("ERROR in BFPRT!  left=%d, right=%d, k=%d\n", left, right, k);
        else{
            int pivot_index = GetPivotIndex(nums, left, right);
            int partition_index = Partition(nums, left, right, pivot_index);
            qpp = partition_index - left + 1;
            if (qpp>k) ret = BFPRT(nums, left, partition_index-1, k);//   partition_index>=left so qpp = partition_index - left + 1 > k 
            else if (qpp<k) ret = BFPRT(nums, partition_index+1, right, k-qpp); 
                    else    ret = nums[partition_index];
        }
        
        return ret;

    }

    int GetPivotIndex(vector<int>& nums, int left, int right){ //不要忘记依次考虑  right-left = 0,1,2,3,4，5的情况
        int left_idx, i = left;
        if (left>right) printf("ERROR in GetPivotIndex! left=%d, right=%d\n", left, right);
        left_idx = left;
        vector<int>::iterator it = nums.begin()+left;
        while (i+4<=right){
            sort(it, it+4);
            if (debug) {printf("%d %d %d %d %d\n", nums[i],nums[i+1],nums[i+2],nums[i+3],nums[i+4]);}
            swap(nums[i+2], nums[left_idx++]);
            i+=5;
            it+=5;
        }
        if (i<right) {
            if (debug) printf("i=(%d %d) right=(%d %d) i+(right-i)>>1=%d ", i, *it,  right, *(nums.begin()+right), i+(right-i)>>1);
            sort(it, nums.begin()+right); 
            swap(nums[i+((right-i)>>1)], nums[left_idx++]); //>>的执行顺序！一开始我写的i+(right-i)>>1 会从左到右执行的
        } 
        if (debug) {
            for (int i=left; i<=right;i++) printf("%d ",nums[i]);
            printf("In GetPivotIndex left=%d, right=%d, left_idx=%d %d\n",left, right, left_idx-1, nums[left_idx-1]);
            }
        return (left_idx-2>left) ? GetPivotIndex(nums, left, left_idx-1) : left;
    }

    int Partition(vector<int>& nums, int left, int right, int pivot_index){
        int i, left_idx = left;
        swap(nums[pivot_index], nums[right]);
        for (int i=left; i<right; i++)
            if (nums[i]<nums[right]) 
                swap(nums[left_idx++], nums[i]);
        swap(nums[left_idx], nums[right]); 
        if (debug) {
            for (int i=left; i<=right;i++) printf("%d ",nums[i]);
            printf("In Partition left=%d, right=%d,  left_idx=%d %d\n",left, right, left_idx, nums[left_idx]);
        }
        return left_idx;

    }
};

//8ms faster than 83.3% 