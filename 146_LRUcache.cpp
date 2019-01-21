#include <iostream>
#include <unordered_map>
#include <vector>
#include <list>
//#include <pair>

using namespace std;
using std::unordered_map;
using std::vector;
using std::list;
//using pair;
int debug = 1;
class LRUCache {
public:
    LRUCache(int capacity): _capacity(capacity){} //这个私有变量666

    int get(int key){
        int val;
        auto it = cache.find(key);
        if (it == cache.end()) val = -1;
        else{
            touch(it);
            val = it->second.first; //所以iterator -> second. first 存的是value
        }
        return val;
    }

    void put(int key, int value){ // key & value的关系一定要搞明白 key并不是指位置，不要在这个地方被迷糊
        auto it = cache.find(key);
        if (it != cache.end()) touch(it);
        else{
            if (cache.size() == _capacity){
                cache.erase(used.back()); 
                if (debug) cout << typeid( used.back() ).name() << endl; // map移除指定值是xx.erase 好奇type(used.back()) 的type是int 
                used.pop_back();  //list的pop最后一个 就是xx.p                
            }
            used.push_front(key);
        }
        cache[key] = {value, used.begin()};
    }

private:
    typedef list<int> LI;
    typedef pair<int, LI::iterator> PII;  //一开始写成了一个冒号： 要去查一下pair的用法了emmm 
    typedef unordered_map<int, PII> HIPII;

    LI used;
    HIPII cache;
    int _capacity;

    void touch(HIPII::iterator it){
        int key = it->first;
        used.erase(it->second.second); 
        if (debug) cout <<it->second.second<< endl; //所以iterator -> scond.second 存的是它在list（used) 中的位置？
        used.push_front(key);
        it->second.second = used.begin();
        if (debug) cout << typeid( used.begin() ).name() << endl;  //好奇 c++ list.begin() 输出的类型到底是什么？ iterator？ 
    }
};


/* https://blog.csdn.net/lskyne/article/details/10418823 

list.begin list.end() 返回指向第1/末尾的iterator
list.erase 删除一个元素
list.back() list.front() 返回最后一个/返回第一个元素
list.unique() 删除重复的元素

list.push_front() list.push_back() 在首尾加入元素
list.pop_front() list.pop_back() 在首尾删除元素
 */
int main(){
    LRUCache* qpp = new LRUCache(2);
    qpp.set(1,2);
    qpp.set(2,3);
    qpp.set(3,4);
    printf("%d", qpp.get(1));
    printf("%d", qpp.get(2));
    qpp.set(1,2);
    printf("%d", qpp.get(3));
}