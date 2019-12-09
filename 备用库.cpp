#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <set>
#include <iterator>


list.begin() list.end()
list.front() list.back()
list.push_front() list.push_back()
list.unique()  删除重复的元素
unordered_map.erase(key)

//初始化vector
vector<vector<bool>> visited(m, vector<bool>(n)); 

vector<int>::iterator v = vec.begin();
   while( v != vec.end()) {
      cout << "value of v = " << *v << endl;
      v++;
   }

v.insert(v.begin(),5);
v.erase(v.begin());

v1.swap(v2); //swap v1 and v2


 queue<pair<int, int>> q; 
 q.front() 
 q.pop()  //pop开头
 q.push() //末尾

 排序：
 int a[10]= {1, 5, 8, 9, 6, 7, 3, 4, 2, 0}; 
 sort(a, a+10);  //即可

 binary_search(startaddress, endaddress, valuetofind)
 e.g. binary_search(a, a+10, 2)


//queue
queue<int> q
q.empty() //returns whether empty
q.push()(e.emplace()) q.pop()
showq(q)
q.front() q.back()

stack <int> s;
s.push()  s.pop()
showstack(s);
s.pop()
s.top()


//set

set<int> st;
pair<set<int>::iterator, bool> ptr;
ptr = st.insert(20);
// checking if the element was already present or newly inserted 
if (ptr.second) 
    cout << "The element was newly inserted" ; 
else cout << "The element was already present" ; 

it = st.begin()
st.erase(it)
st.erase(value) 
