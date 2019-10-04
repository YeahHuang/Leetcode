class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp = []
        while self.stack:
            num = self.stack.pop()
            if self.stack:
                tmp.append(num)
        while tmp:
            self.stack.append(tmp.pop())
        return num
    

    def peek(self) -> int:
        """
        Get the front element.
        """
        tmp = []
        while self.stack:
            num = self.stack.pop()
            tmp.append(num)
        while tmp:
            self.stack.append(tmp.pop())
        return num

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()