class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.list = [0]*size
        self.sum = 0
        self.cur_idx = 0
        self.is_full = False

    def next(self, val: int) -> float:
        if self.is_full:
            self.sum = self.sum - self.list[self.cur_idx] + val
            self.list[self.cur_idx] = val
            self.cur_idx = (self.cur_idx + 1) % self.size
            return self.sum / self.size
        else:
            self.sum += val
            self.list[self.cur_idx] = val
            self.cur_idx += 1
            if self.cur_idx == self.size:
                self.is_full = True
                self.cur_idx = 0 
            return self.sum / self.cur_idx if self.cur_idx>0 else self.sum / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)