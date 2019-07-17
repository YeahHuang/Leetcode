class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool: #40ms
        intervals.sort(key = lambda x: x[0])
        flag = True
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                flag = False
                break
        return flag
