class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m, n, step=0, cnt=0;
        m = grid.size();
        n = grid[0].size();
        queue<pair<int, int>> q;
        vector<pair<int,int>> dir = {{-1,0},{1,0},{0,-1},{0,1}};
        for (int i=0; i<m; i++)
            for (int j=0; j<n; j++)//WA1 写成了 j<m
                if (grid[i][j] == 1)
                    cnt += 1;
                else if (grid[i][j] == 2)
                    q.push({i,j});
        while (!q.empty()){
            if (cnt==0)
                return step;
            step += 1;
            int size = q.size();
            for (int i=0; i<size; i++)
            {
                pair<int, int> p = q.front();
                q.pop();
                for (int j=0;j<4;j++){
                    int x = p.first+dir[j].first;
                    int y = p.second + dir[j].second;
                    if (x<0 || x>=m || y<0 || y>=n || grid[x][y]!=1) continue;
                    grid[x][y] = 2;
                    cnt -= 1;
                    q.push({x,y});
                }
            }
        
        }
        if (cnt>0) return -1;
        return step;
    }
    

};