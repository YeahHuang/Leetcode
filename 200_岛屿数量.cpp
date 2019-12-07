class Solution {
public:
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    int numIslands(vector<vector<char>>& grid) {
         int qpp, num_island;
         num_island = 0; 
         m = grid.size();
         if (m>0){
            n = grid[0].size();
            for (int i=0;i<m;i++)
                for (int j=0;j<n;j++)
                    if (grid[i][j]=='1'){
                        num_island+=1;
                        //colorGrid_DFS(grid, i, j, num_island + 1);
                        colorGrid_BFS(grid, i, j);
                    }
         }
         return num_island;
    }

    
private:
    int m,n;
    

    void colorGrid_BFS(vector<vector<char>>& grid, int x, int y){
        queue<vector<int>> q; //一开始写的queue<vector> 卡了特别特别久
        q.push({x,y});
        grid[x][y] = '0';
        while (!q.empty()){
            x = q.front()[0];
            y = q.front()[1];
            q.pop();
            if (x>0 && grid[x-1][y]=='1') {q.push({x-1,y}); grid[x-1][y]='0';};
            if (x<m-1 && grid[x+1][y]=='1') {q.push({x+1,y}); grid[x+1][y]='0';}; //一开始写成了x<m-1! 范围问题 是否有等于号的问题 一定要看清楚分清楚啊！
            if (y>0 && grid[x][y-1]=='1') {q.push({x,y-1}); grid[x][y-1]='0';};
            if (y<n-1 && grid[x][y+1]=='1') {q.push({x,y+1}); grid[x][y+1]='0';};
        }
    }



     void colorGrid_DFS(vector<vector<char>>& grid, int x, int y){
        if (x<0 || x>=m || y<0 || y>=n){
           // cout << "ERROR! (" << x << ',' << y <<') Out of Range!!!'<<endl;
        }
        grid[x][y] = 0;
        if (x>0 && grid[x-1][y]=='1')  colorGrid_DFS(grid, x-1, y);
        if (x<m-1 && grid[x+1][y]=='1') colorGrid_DFS(grid, x+1, y);
        if (y>0 && grid[x][y-1]=='1') colorGrid_DFS(grid, x, y-1);
        if (y<n-1 && grid[x][y+1]=='1') colorGrid_DFS(grid, x, y+1);
        
        /*
        int x1,y1;
        for (int i = 0; i<4; i++)
        {
            x1 = x + dx[i];
            y1 = y + dy[i];
            if (inBound(x1, y1) && grid[x1][y1]==1)
                colorGrid_DFS(grid, x1,y1,color_id);
        }*/
    }

    bool inBound(int x, int y){
        return ( x>=0 && x<m && y>=0 && y<n);
    }
};

//DFS 12ms(>59.6%) BFS 20ms 然后写的长一些 可以变快一点。 不用一直调用inbound



#include <iostream>
#include <vector>
#include <queue>

using namespace std;

/*
1. iterate over the binaryMatrix
2. matrix[i][j] = 0 do nothing
3. matrix[i][j] = 1 dfs numIsland+1 
    -> marked adjacent to visited(mark the numer from 1 -> 2)
4. do the iteration again (step 1)
*/

// push()
// pop()
// front()



int getNumberOfIslands( const vector<vector<int>>& mat ) 
{
  // your code goes here
  /*m - matrix.length
  n - matrix[i].length 
    O(mn)  */
  
  int m = mat.size();
  int n = mat[0].size(); //一开始写成mat[1]了
  //initialize visited
  vector<vector<bool>> visited(m, vector<bool>(n)); //这样初始化酷很多
  
  /*vector<bool> tmp;
  for (int j=0; j<n; j++)
      tmp.push_back(false);
  for (int i=0; i<m; i++)
      visited.push_back(tmp);*/
  
    
  vector<pair<int, int>> dir = {{1,0}, {-1,0}, {0,-1},{0,1}};
    
    
  //iterate the matrix
  int numIs = 0;
  for (int i=0; i<m; i++)
    for (int j=0; j<n; j++)
      if (mat[i][j]==1 && !visited[i][j])  //cell is land and unvisited
      {
        numIs++;
        //expand(i,j);
        //vector<pair<int, int>> stack; 不应该是stack 应该是一个queue
        queue<pair<int, int>> q; 
        visited[i][j] = true;
        q.push({i,j});
        while (!q.empty()){ //用 ！代替==false
          auto cur = q.front(); //(cur.first, cur.second) 一开始忘记写type了 
          q.pop();
          for (auto d: dir){
            int x = d.first + cur.first;
            int y = d.second + cur.second;
            if (0<=x && x<m && 0<=y && y<n && mat[x][y]==1 && !visited[x][y]){
              visited[x][y] = true;
              q.push({x,y});
            }
          } 
        }
      }
  
  return numIs;
}

int main() {
  
  
  return 0;
}