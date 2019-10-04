class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int: 
        """
        Removes the element on top of the stack and returns that element.
        """
        tmp_queue = collections.deque()
        while self.queue:
            num = self.queue.popleft()
            if self.queue:
                tmp_queue.append(num)
        self.queue = tmp_queue
        return num

    def top(self) -> int:
        """
        Get the top element.
        """
        tmp_queue = collections.deque()
        while self.queue:
            num = self.queue.popleft()
            tmp_queue.append(num)
        self.queue = tmp_queue
        return num
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue)==0

#Sol2 倒置的话似乎更短一些 因为这里同时有pop&top 都只需要queue[0], queue popleft了
#但都是36ms
class Stack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        
    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]
    
    def empty(self):
        return not len(self._queue)
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()