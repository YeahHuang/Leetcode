#from collections import defaultdict

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.defaultdict() #可以修改为 self.data = collections.defaultdict(list)

    def findIdx(self, arr: list, timestamp):
        l,r = 0, len(arr)-1
        while l<=r:  
            mid = (l+r)//2                
            if arr[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return r

    def set(self, key: str, value: str, timestamp: int) -> None:
        '''
        #Improved: 这里的timestamp是默认单调递增的 所以不用测排序
        #仅仅优化这个可以 1056ms -> 832ms
        if key in self.data.keys(): #Improved: 这里的timestamp是默认单调递增的 所以不用测排序
            self.data[key].insert(self.findIdx(self.data[key], timestamp)+1, (value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]
        '''
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        if key in self.data.keys() and timestamp>=self.data[key][0][1]:
            ret = self.data[key][self.findIdx(self.data[key], timestamp)][0]
        return ret

class TimeMap: #用bisect代替我自己的插入 可以832ms-> 764ms
    def __init__(self):
        self.data = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.data[key].append((timestamp, value))

    def get(self, key, timestamp):
        A = self.data.get(key, None)
        if A is None: return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i-1][1] if i else ""

