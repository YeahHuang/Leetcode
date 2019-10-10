class Solution:
    #Sol1 我就是慢慢分析了 l = 0, l = len(interval) 96ms
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        left = [interval[0]  for interval in intervals]
        right = [interval[1]  for interval in intervals]
        l = bisect.bisect_left(left, newInterval[0])
        if l == len(intervals):
            if newInterval[0]<= intervals[-1][1]:
                intervals[-1][1] = max(intervals[-1][1],newInterval[1])
            else:
                intervals.append(newInterval)
            return intervals
        if l>0 and newInterval[0] < intervals[l][0] and newInterval[0]<=intervals[l-1][1] :
            newInterval[0] = intervals[l-1][0]
            l -= 1
        if l == 0 and newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        while len(intervals)>l and intervals[l][1]<= newInterval[1]:
            intervals.pop(l)
        if len(intervals) == l or newInterval[1]<intervals[l][0]:
            intervals.insert(l, newInterval)
        else:
            intervals[l][0] = newInterval[0]
        return intervals
        
        '''
            else:
                while len(intervals) and intervals[0][1]<= newInterval[1]:
                    intervals.pop(0)
                if len(intervals) == 0:
                    intervals.append(newInterval)
                elif newInterval[1]>=intervals[0][0]:
                    intervals[0][0] = newInterval[0]
                else:
                    intervals.insert(0, newInterval)
        '''
    #Improved 用的别人的优雅的代码 88ms
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret, n = [], newInterval
        for idx, i in enumerate(intervals): #一开始错误的写成了i, idx 
            if n[1] < i[0]:
                return ret + [n] + intervals[idx:]
            elif n[0]> i[1]:
                ret.append(i)
            else:
                n[0] = min(n[0], i[0])
                n[1] = max(n[1], i[1])
        return ret + [n]
