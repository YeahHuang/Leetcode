class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        def findIdx(num, rooms):
            if rooms==[]:#WA 因为一开始没写着咧当只有1个的时候不能直接判断[-1]
                return 0
            if num>rooms[-1]:
                return len(rooms)
            else:
                l = 0
                r = len(rooms)-1
                insert_flag = False
                while l<=r:
                    m = (l+r)//2
                    if (m and rooms[m]>=num>=rooms[m-1]) or (m==0 and rooms[m]>num):
                        #rooms.insert(m, intervals[i][1])         
                        insert_flag = True
                        return m
                    elif rooms[m] < intervals[i][1]:
                        l = m + 1
                    else:
                        r = m - 1
                if insert_flag==False:
                    print("ERROR! num=%d l=%d r=%d"%(num, l, r))
                    print(rooms)
                    j = len(rooms) - 1
                    while j>=0 and rooms[j]>num:
                        j -= 1
                    return j+1
                    #print("ERROR! i=%d, l=%d r=%d [%d %d]"%(i,l,r,intervals[i][0], intervals[i][1]))
        #现在在想 其实只不是只要找到重叠的部分最多重叠了多少个interval就好了
        #一个个meeting rooms 实际的new 出来 发现重叠啦 选择目前不重叠的 但是largest 放进去
        #关于维护目前的end pos, 可以用heapq 也可以插入排序 也可以直接
        if intervals == []: return 0
        debug = False
        intervals.sort(key = lambda x:x[0])
        rooms = [intervals[0][1]]
        if debug:
            print(rooms)
        for i in range(1, len(intervals)):
            if intervals[i][0] < rooms[0]: #比最早的end pos 都小了 那必须new了吖
                rooms.append(intervals[i][1])
                rooms.sort() #52ms
                ''' 48ms
                idx = findIdx(intervals[i][1],rooms)
                rooms.insert(idx, intervals[i][1])
                if debug:
                    print(intervals[i])
                    print("insert into %d"%idx)
                    print("now rooms", rooms)
                '''
                
                #if insert_flag==False:
                #   print("ERROR! i=%d, l=%d r=%d [%d %d]"%(i,l,r,intervals[i][0], intervals[i][1]))
            else:
                idx = findIdx(intervals[i][0],rooms) - 1
                rooms.pop(idx)
                idx = findIdx(intervals[i][1],rooms)
                rooms.insert(idx, intervals[i][1])
                #rooms[idx] = intervals[i][1] #一开始写成了这个 而忘记了sort WA
                #rooms.sort() 
                if debug:
                    print("room[%d]=%d i=%d start=%d"%(idx, intervals[i][1], i,intervals[i][0]))
        return len(rooms)
                   

    #Sol1.1 简化好看版
        def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        def findIdx(num, rooms):
            if rooms==[]:   return 0 #WA 因为一开始没写着咧当只有1个的时候不能直接判断[-1]
            if num>rooms[-1]:
                return len(rooms)
            else:
                l = 0
                r = len(rooms)-1
                insert_flag = False
                while l<=r:
                    m = (l+r)//2
                    if (m and rooms[m]>=num>=rooms[m-1]) or (m==0 and rooms[m]>num):
                        return m
                    elif rooms[m] < intervals[i][1]:
                        l = m + 1
                    else:
                        r = m - 1
                if insert_flag==False:
                    j = len(rooms) - 1
                    while j>=0 and rooms[j]>num:
                        j -= 1
                    return j+1

        if intervals == []: return 0
        debug = False
        intervals.sort(key = lambda x:x[0])
        rooms = [intervals[0][1]]
        if debug:
            print(rooms)
        for i in range(1, len(intervals)):
            if intervals[i][0] < rooms[0]: #比最早的end pos 都小了 那必须new了吖
                #48ms
                idx = findIdx(intervals[i][1],rooms)
                rooms.insert(idx, intervals[i][1])
            else:
                rooms.pop(0)#不知道为什么这里如果插入的话反而会慢
                rooms.append(intervals[i][1])
                rooms.sort() 
                
        return len(rooms)

    #Sol2 heapq 代替我的插入排序 44ms
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals == []: return 0
        intervals.sort(key = lambda x:x[0])
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for interval in intervals[1:]:
            if interval[0] < rooms[0]:
                heapq.heappush(rooms, interval[1])
            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms, interval[1])
        return len(rooms)
