class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        s.push(x); 
        if (smin.empty() || x<=smin.top()) smin.push(x);//一开始写成了!smin  以后要注意栈和这些东西不要弄混了
    }
    
    void pop() {
        if (s.top()==smin.top()) smin.pop();
        s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return smin.top();
    }
private:
    stack<int> s;
    stack<int> smin;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */