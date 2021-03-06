class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.w = collections.defaultdict(int)        

    def shouldPrintMessage(self, timestamp: int, msg: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if self.w.get(msg) is None or timestamp - self.w[msg]>=10:
            self.w[msg] = timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)