#Sol1 my 
class LogSystem:

    def __init__(self):
        self.records = []
    
    def put(self, id: int, timestamp: str) -> None:
        bisect.insort_left(self.records, (timestamp, id))

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        '''
        if gra == 'Minute': 一开始这么写 会曝出 string does not support item assignment
            s[-2:] = '00'
            e[-2:] = '59'
        elif gra == 'Hour':
            s[-5:] = '00:00'
            e[-5:] = '59:59'
        elif gra == 'Day':
            s[-8:] = '00:00:00'
            e[-8:] = '23:59:59'
        elif gra == 'Month':
            s[-11:] = '01:00:00:00'
            e[-11:] = '31:23:59:59'
        elif gra == 'Year':
            s[-13:] = '01:01:00:00:00'
            e[-13:] = '12:31:23:59:59'
        '''
        if gra == 'Minute':
            s = s[:17] + '00'
            e = e[:17] + '59'
        elif gra == 'Hour':
            s = s[:14] + '00:00'
            e = e[:14] + '59:59'
        elif gra == 'Day':
            s = s[:11] + '00:00:00'
            e = e[:11] + '23:59:59'
        elif gra == 'Month':
            s = s[:8] + '01:00:00:00'
            e = e[:8] + '31:23:59:59'
        elif gra == 'Year':
            s = s[:5] + '01:01:00:00:00'
            e = e[:5] + '12:31:23:59:59'
        l = bisect.bisect_left(self.records, (s, 0))
        r = bisect.bisect_right(self.records, (e, float('inf')))
        return [id for (_, id) in self.records[l:r]]

#Sol2: 64ms 更简洁 直接比较
class LogSystem(object):
    def __init__(self):
        self.logs = []

    def put(self, tid, timestamp):
        self.logs.append((tid, timestamp))
        
    def retrieve(self, s, e, gra):
        index = {'Year': 5, 'Month': 8, 'Day': 11, 
                 'Hour': 14, 'Minute': 17, 'Second': 20}[gra] #这个可以学一下了
        start = s[:index]
        end = e[:index]
        
        return [tid for tid, timestamp in self.logs
                      if start <= timestamp[:index] <= end]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)