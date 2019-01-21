class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        bool ret;
        if (hash.find(val)!=hash.end()) ret=false;
        else {
            v.push_back(val); 
            //他用的是v.emplace_back(val) v.push_back 72ms v.emplace_back 50ms

            /*
            https://blog.csdn.net/xiaolewennofollow/article/details/52559364 
            emplace only constructed;    move constructed&moved
            所以emplace更快！
            http://www.cplusplus.com/reference/vector/vector/emplace_back/ 
            具体的之后可以详细了解一下！
            */
            hash[val] = v.size()-1;
            ret = true;
        }
        return ret;
    }

    bool remove(int val) {
        bool ret;
        if (hash.find(val)==hash.end()) ret=false;
        else{
            int last = v.size()-1;
            hash[v[last]] = hash[val];
            swap(v[last], v[hash[val]]);
            v.pop_back();
            hash.erase(val);
            ret = true;
        }   
        return ret;
    }
    /** Get a random element from the set. */
    int getRandom() {
        return v[rand()%v.size()];
    }
private:
    unordered_map<int,int> hash;
    vector<int> v;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */

/*original mine

bool insert(int val) {
        bool ret;
        if (hash.find(val)==hash.end()) {
            ret = true;
            hash[val] = true;
        }
        else {
            ret = false;
        }
        return ret;
    }
    
   
    bool remove(int val) {
        if (hash.find(val)!=hash.end()) {
            ret = true;
            hash.erase(val);
        }
        else ret=false;
        return ret;
    }
*/