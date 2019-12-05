/*
We simulate each day of the prison.

Because there are at most 256 possible states for the prison, eventually the states repeat into a cycle rather quickly. We can keep track of when the states repeat to find the period t of this cycle, and skip days in multiples of t.

Algorithm

Let's do a naive simulation, iterating one day at a time. For each day, we will decrement N, the number of days remaining, and transform the state of the prison forward (state -> nextDay(state)).

If we reach a state we have seen before, we know how many days ago it occurred, say t. Then, because of this cycle, we can do N %= t. This ensures that our algorithm only needs O(2∗∗cells.length) steps.
*/

class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        unordered_map<int, int> map;
        map[cells2Int(cells)] = 0;
        bool findCycle = false;
        for (int i=1; i<=N; i++){
            vector<int> tmp;
            tmp.push_back(0);
            for (int j=1; j<7; j++){
                tmp.push_back(int(cells[j-1] ^ cells[j+1] == 0));
            }
            tmp.push_back(0);
            if (findCycle==false){
                if (map.find(cells2Int(tmp)) == map.end())
                    map[cells2Int(tmp)] = i;
                else{
                    int cycle = i-map[cells2Int(tmp)];
                    N = (N-i)%cycle + i; //WA1 写成了N%cycle
                    findCycle = true;
                }
            }
            cells = tmp;
        }
        return cells;
    }
private:
    int cells2Int(vector<int>& cells){
        int ret = 0;
        for (int i=0; i<8; i++)
            if (cells[i] == 1)
                ret += 1<<i;
        return ret;
    };
};