#include <unordered_map>
#include <iostream> 
#include <vector>

using std::unordered_map;
using std::vector;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        int qpp, a, b, c, low, high,n,sum,i;
        sort(nums.begin(), nums.end()); 
        //nums.erase(unique(nums.begin(), nums.end()), nums.end()); 一开始没理解对题意， 它说的非重复 是3元素非重复。
        n = nums.size(); //一开始忘记声明 n, low， high
        i = 0;
        while (i<n)
        {
            a = nums[i];
            low = i + 1;
            high = n - 1;
            while (low<high){
                sum = nums[i] + nums[low] + nums[high];
                if (sum == 0)
                {
                    vector<int> v;
                    v.push_back(nums[i]);
                    v.push_back(nums[low]);
                    v.push_back(nums[high]);
                    ans.push_back(v);
                    low ++;
                    high --;
                    while (low  < n && nums[low]==nums[low-1]) low++; //更新模式2次弄错 一次WA因此
                    while (high >=0 && nums[high]==nums[high+1]) high--;
                }
                else if (sum>0) {high--; while (high >=0 && nums[high]==nums[high+1]) high--;}
                        else    {low++; while (low < n && nums[low]==nums[low-1]) low++;}
                
            }
            i++;
            while ( i<n && nums[i]==nums[i-1]) i++;
        }
        return ans;
    }
};
//144 ms faster than 25%


/* 104ms faster than 61.22% 我觉得if的顺序也很重要。
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
      if (nums.size() == 0) return {};
      
      vector<vector<int>> zeroed;
      
      sort(nums.begin(), nums.end());
      
      int i = 0;
      while (nums[i] <= 0 && i < nums.size()) {
        if (i > 0 && nums[i] == nums[i - 1]) {
          ++i; 
          continue;
        }
        
        int begin = i + 1;
        int end = nums.size() - 1;
        
        while (begin < end) {
          int sum = nums[begin] + nums[end];
          
          if (sum < -nums[i] ) begin++;
          else if (sum > -nums[i]) end--;
          else {
            zeroed.push_back({nums[i], nums[begin], nums[end]});
          
            while (begin < end && nums[begin] == zeroed.back()[1]) begin++;
          }
        }
        
        ++i;
      }
      
      return zeroed;
    }
};
*/