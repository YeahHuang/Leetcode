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

/*
time happy algorithm
space heavy approach
O(1) 查找 —> hashmap
O(1) 删除 -> double linked list
*/
int debug = 1;
class LRUCache {
public:
    LRUCache(int capacity): _capacity(capacity){} //这个私有变量666

    int get(int key){
        int val;
        auto it = m_map.find(key);
        if (it == m_map.end()) val = -1;
        else{
            touch(it);
            val = it->second.first; //所以iterator -> second里存的是PII first存的是value
        }
        return val;
    }

    void put(int key, int value){ // key & value的关系一定要搞明白 key并不是指位置，不要在这个地方被迷糊
        auto it = m_map.find(key);
        if (it != m_map.end()) touch(it); //unordered_map find constant time 
        else{
            if (m_map.size() == _capacity){
                m_map.erase(m_list.back()); 
                if (debug) cout << typeid( m_list.back() ).name() << endl; // map移除指定值是xx.erase 好奇type(m_list.back()) 的type是int 
                m_list.pop_back();  //list的pop最后一个 就是xx.p                
            }
            m_list.push_front(key);
        }
        m_map[key] = {value, m_list.begin()};
    }

private:
    list<int>  m_list; //记录key的list
    typedef pair<int, list<int>::iterator> PII;   //PII第一个value 第二个为key对应的位置 
    typedef unordered_map<int, PII> HIPII;  //第一个key 第二个它在list中的位置 
    HIPII m_map;
    int _capacity;

    void touch(HIPII::iterator it){ //把当前那个已经在m_map里的it 移到第一个
        int key = it->first;
        m_list.erase(it->second.second); 
        if (debug) cout <<it->second.second<< endl; 
        //所以iterator -> scond.second 存的是它在list（m_list) 中的位置
        m_list.push_front(key);
        it->second.second = m_list.begin();
        if (debug) cout << typeid( m_list.begin() ).name() << endl;  //好奇 c++ list.begin() 输出的类型到底是什么？ iterator？ 
    }
};

//Sol improved 用slice 自己写的 很快乐
//超厉害！！！m_list.splice(m_list.begin(), m_list, found_iter->second); 

//http://www.cplusplus.com/reference/list/list/splice/ 晚点再看
//https://stackoverflow.com/questions/13837121/functioning-of-splice-in-cpp
class LRUCache {
    
public:
    LRUCache(int capacity): _capacity(capacity){}

    int get(int key){
        /*
        if not found return -1
        if found return val + put iter to front 
        */
        int val;
        //pair<int, int>::iterator found_iter = m_map.find(key) WA!!!
        //found_iter != m_map[key]    found_iter -> second 才是那个iterator
        //所以如果要在这里定义found_iter 只能auto
        if (m_map.find(key) == m_map.end())
            val = -1;
        else{
            //pair<int, int>::iterator found_iter = m_map[key]; error: 'iterator' is not a member of std:pair<int,int>

            //printf(typeid(found_iter).name()); 实际类型是St14_List_iteratorISt4pairIiiEE
            auto found_iter = m_map[key]; //还是auto稳

            val = found_iter->second;
            m_list.splice(m_list.begin(), m_list, found_iter);
        }
        return val;
    };

    void put(int key, int val){
        //printf("put %d %d", key, val);
        if (m_map.find(key) == m_map.end()){ //not in list
            m_list.push_front(make_pair(key, val));
            m_map[key] = m_list.begin();
            if (m_list.size() > _capacity){
                //m_map.erase(m_list.back() -> first);  WA first back是真实的pair 不是pointer 所以就是.了
                m_map.erase(m_list.back().first);
                m_list.pop_back();
            }
        } else{                             //already in list
            //pair<int, int>::iterator found_iter = m_map[key];
            auto found_iter = m_map[key];
            found_iter -> second = val;//一开始漏写了 你都不改value了咩
            m_list.splice(m_list.begin(), m_list, found_iter);
            
        };
    };
private:
    int _capacity;
    unordered_map<int, list<pair<int,int>>::iterator> m_map;
    list<pair<int, int>> m_list;
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