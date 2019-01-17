/*class Solution {
public:
    int trap(vector<int>& height) {
        int q,p1,p2,n, ans;

        //sort -> 当前最大值 -> 用unique.erase 把max的连续的点都抹掉，只剩下一个。 

        //若 Max=1。左右 除非完全递增/减 则 必有一个 
        //理论上 第一 第二个之间是可以积水的。 问题是第2要选哪个 第1又要选哪个。 //不如排序的时候就1st 大小 2st 位置好了。
        //生命值 -= 1 
        //
        n = height.size();
        ans = 0;
        if (n>2)
        {
            vector<int> sum(n,0);
            sum[0] = height[0];
            for (int i=1;i<n;i++) 
                sum[i] = sum[i-1] + height[i];
            p1 = p2 = -1;
            if (height[0]>height[1]) 
                p1 = 0;
            for (int i=1; i<n-1; i++){
                if (height[i]>height[i-1] && height[i]>height[i+1]){
                    if (p1==-1) 
                        p1 = i;
                    else{
                        p2 = i;
                        ans += min(height[p1],height[p2]) * (p2 - p1-1) - (sum[p2-1] - sum[p1]);
                        p1 = p2;
                    }
                }
            }  
            if (height[n-1] > height[n-2] && p1!=-1){
                p2 = n-1;
                ans += min(height[p1],height[p2]) * (p2 - p1-1) - (sum[p2-1] - sum[p1]);
            }           
        }        
        return ans;
    }
};*/


class Solution {
public:
    int trap(vector<int>& height) {
        int q,p1,p2,n, ans = 0;
        n = height.size();
        if (n>2){
            vector<int> max_left(n,0), max_right(n,0);
            max_left[0] = height[0]; 
            for (int i=1; i<n; i++)
                max_left[i] = max(max_left[i-1], height[i]);
            max_right[n-1] = height[n-1];
            for (int i=n-2; i>0; i--)
                max_right[i] = max(max_right[i+1], height[i]);
            for (int i=1; i<n-1; i++)
                ans += min(max_right[i], max_left[i]) - height[i];
        }

        return ans;
    }
};
/*

 [10, 0,1,0,1,0,1,0,9]
[1,1,1,1,1,0,0,1,1,1,0,1,0]
[0,1,1,1,2, 1, 0] ANs=0
[0,1,1,1,0,1,1,1,2,0,0] gg了
0 1 1 1 0 1 1 1 2 0 0 ANs=1

发现不仅有这个case 极小值并不一定OK
是否应该从两端入宽搜？
是否应该把值从大到小排序？
   
0
1
2

[]

[0,2,0]
[1,2]
*/