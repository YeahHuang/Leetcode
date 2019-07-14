class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        #self.nums =[1, 5, 6, 6, 8, 10, 11, 11, 12, 13, 14, 15, 17, 17]
        self.n = len(self.nums)
        
    def addNum(self, num: int) -> None:
        l = 0
        r = self.n - 1
        m = (l+r)//2
        debug = False
        while l<r:      
            if debug: 
                print(l,r,m,self.nums[m])
            if m==0:
                if num<self.nums[0]:
                    self.nums.insert(0, num)
                elif num<self.nums[1]:
                    self.nums.insert(1,num)
                break
            if (m>0 and self.nums[m]>= num >= self.nums[m-1]):
                self.nums.insert(m, num)
                break
            elif num < self.nums[m-1]:
                r = m-1
            else:
                l = m+1
            m = (l+r)//2
        if len(self.nums)==self.n:
            if self.n>0:
                if num < self.nums[m]:
                    self.nums.insert(m, num)
                else:
                    self.nums.append(num)
            else:
                self.nums.append(num)
        self.n += 1
        
    def findMedian(self) -> float:
        #print(self.nums)
        if self.n%2 == 1:
            return self.nums[self.n//2]
        else:
            return (self.nums[self.n//2]+self.nums[self.n//2-1])/2

    #平衡树 AVL树 大法好 明天补充吧 毕竟hard题
from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self,num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small): #保持二者平衡
            heappush(large, -heappop(small)) #为什么这里是减呢？

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return flat(large[0])
        return (large[0]-small[0])/2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()