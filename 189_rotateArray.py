class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotateOnce(nums, n):
            tmp = nums[n-1]
            '''
            for i in range(1,n):
                nums[i] = nums[i-1]
            会错误的输出[7, 1,1,1,1,1] 要注意覆盖问题啊
            '''
            for i in range(n-1, -1, -1):
                nums[i] = nums[i-1]
            nums[0] = tmp

        n = len(nums)
        k = k%n
        
        #Sol1 48ms 13.5M
        nums[:] = nums[n-k:] + nums[:n-k] #或者 nums[:] = nums[-k:] + nums[:-k]
        

        '''
        #Sol2  48ms 13.4M
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        nums.reverse()

        Sol2 c++ 
        void rotate(vector<int>& nums, int k){
            k%=nums.size();
            reverse(nums.begin(), nums.begin()+k)
            reverse(nums.begin()+k, nums.end())
            reverse(nums.begin(), nums.end())
        }
        '''

        '''
        #
        Sol3 pythonic solutions:  48ms 13.2M
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        
        Sol4 deque . 52ms 13.7M
        d = collections.deque(nums)
        d.rotate(k)
        nums[:] = list(d)
        '''

        '''
        Sol5
        for i in range(k):      #120ms 13.4M
            nums.insert(0, nums[-1])
            nums.pop()
        for i in range(k):      #2452ms 13.5M
            nums[:] = [nums.pop()]+nums

        '''


        '''
        这样会TLE
        for i in range(k):
            rotateOnce(nums, n) 
        ''' 

'''
java
public class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        int count = 0;
        for (int start = 0; count < nums.length; start++) {
            int current = start;
            int prev = nums[start];
            do {
                int next = (current + k) % nums.length;
                int temp = nums[next];
                nums[next] = prev;
                prev = temp;
                current = next;
                count++;
            } while (start != current);
        }
    }
}

关于python的slice
>>> a = [1,2,3,4,5,6]
>>> a
[1, 2, 3, 4, 5, 6]
>>> a[::0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: slice step cannot be zero
>>> a[::1]
[1, 2, 3, 4, 5, 6]
>>> a[::-1]
[6, 5, 4, 3, 2, 1]
>>> a[::2]
[1, 3, 5]
>>> a[::-2]
[6, 4, 2]
>>> a[::5]
[1, 6]
>>> a[::6]
[1]
>>> a[::-7]
[6]
'''


