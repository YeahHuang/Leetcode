#include <stack>

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack_paren;
        bool flag = true;
        for ( char& c : s){  //这个for用法很棒
            switch (c){
                case '(':
                case '{':
                case '[': stack_paren.push(c);break;
                case ')': if (stack_paren.empty() || stack_paren.top()!='(') flag = false; else stack_paren.pop(); break; //stack自带的.push .top .empty.pop需要熟练呀
                case '}': if (stack_paren.empty() || stack_paren.top()!='{') flag = false; else stack_paren.pop(); break; //一开始忘记了.pop
                case ']': if (stack_paren.empty() || stack_paren.top()!='[') flag = false; else stack_paren.pop(); break;
                default: ;  // switch case default不能忘
            }
            if (!flag) break;
        }
        if (!stack_paren.empty()) flag = false; //最后的.empty不能忘
        return flag;
    }
};