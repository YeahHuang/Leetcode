class Solution {
public:
    /*
    1. traverse the graph
    2. if it's land & unvisited -> cur_color++,  expand the cur land to color the suurrounding land with cur_color
    3. cur_color starts with 2. visited lands marked with 2 unvisited land marked with 1, water marked with 0
    4. finally, return cur_color - 1 
    */
    int numIslands(vector<vector<char>>& grid) {
        if (grid.size() == 0)
            return 0;
        vector<pair<int, int>> dir = {{1,0},{0,1},{-1,0},{0,-1}};
        int cur_color = 1;
        int m, n;
        m = grid.size();
        n = (grid[0].size());
        for (int i=0; i<m; i++)
            for (int j=0; j<n; j++){
                if (grid[i][j] == '1') {
                    vector<pair<int,int>> stack; //D1 忘记在里头写pair了
                    stack.push_back(make_pair(i, j)); 
                    cur_color ++;
                    while (stack.size()){
                        pair<int,int> cur = stack.back();  //如何获得最后一个元素并pop？ 
                        stack.pop_back();
                        for (auto d: dir){
                            int x = cur.first+d.first;
                            int y = cur.second + d.second;
                            if (x>=0 && x<m && y>=0 && y<n && grid[x][y] == '1'){
                                stack.push_back(make_pair(x,y));
                                grid[x][y] = '2'; //一开始想写成 2，3，4...后来才发现不行 
                            }                 
                        }
                    };    
                }
        }
        return cur_color - 1;
    }
};