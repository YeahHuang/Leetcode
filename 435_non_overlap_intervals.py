class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        1. 先sort intervals
        2. 用t[i][j] 表示 i&j有link 注意 这肯定是有序的 我觉得发现没overlap后贪心就行了
        用hash pop i 然后把更少的依次扔出来
        ps 优化：我发现不用判断在不在里头 直接减就是了 
        '''
        end_pos = -2147483647 #float('-inf')
        debug = False
        ori_len = len(intervals)
        '''
        valid = [True for i in range(len(intervals))]
        
        for i in range(len(intervals)):
            if valid[i]:
                for j in range(i+1, len(intervals)):
                    if intervals[i][0] == intervals[j][0] and intervals[i][1] == intervals[j][1]:
                        valid[j] = False
        print(valid)
        tmp = []
        for i in range(len(intervals)):
            if valid[i]:
                tmp.append(intervals[i])
        intervals = tmp
        erase_num = ori_len - len(intervals)
        if debug:
            print(erase_num)

        #WA case: [[0, 2], [1, 3], [1,3], [2, 4], [3, 5],[3,5], [4, 6]] 
        去重自然是一个good solution 但是会TLE
        可能还是需要注意 你一定是让 end_pos 尽量的小 才best 吖
        '''
        erase_num = 0
            
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        start_idx = 0
        
        lap = [[] for i in range(len(intervals))]
        for i, interval in enumerate(intervals):
            if interval[0] < end_pos:
                end_pos = max(end_pos, interval[1])
                for j in range(start_idx, i):
                    if interval[0] < intervals[j][1]:
                        lap[j].append(i)
                        lap[i].append(j)
            else:
                #处理上一段关系
                delete = {}
                len_lap = [0 for j in range(len(intervals))]
                if debug:
                    print("start_idx = %d i=%d"%(start_idx, i))
                for j in range(start_idx, i):
                    if debug:
                        print(j)
                    len_lap[j] = len(lap[j])
                    if len_lap[j]:
                        delete[j] = len_lap[j]
                while delete:
                    max_len = -1
                    for j in delete.keys():
                        if len_lap[j] > max_len:
                            max_len = len_lap[j]
                            del_idx = j
                    delete.pop(del_idx)
                    erase_num += 1
                    for j in lap[del_idx]:
                        if j in delete.keys():
                            len_lap[j] -= 1
                            if len_lap[j] <= 0:
                                delete.pop(j)
                #开启下一段关系的初始化 
                start_idx = i
                end_pos = interval[1]
        if start_idx != len(intervals)-1:
            if 1>0:
                delete = {}
                len_lap = [0 for j in range(len(intervals))]
                if debug:
                    print("start_idx = %d i=%d"%(start_idx, i))
                    print(intervals)
                for j in range(start_idx, len(intervals)):
                    len_lap[j] = len(lap[j])
                    if len_lap[j]:
                        delete[j] = len_lap[j]
                if debug:
                    print(lap)
                    print(len_lap)
                while delete:
                    if debug:
                        print(delete)
                    max_len = -1
                    for j in delete.keys():
                        if len_lap[j] > max_len:
                            max_len = len_lap[j]
                            del_idx = j
                    delete.pop(del_idx)
                    erase_num += 1
                    for j in lap[del_idx]:
                        if j in delete.keys():
                            len_lap[j] -= 1
                            if len_lap[j] <= 0:
                                delete.pop(j)
        return erase_num

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int: #算法层面 你必然要选择数量少的。 
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[0])
        curr_end, cnt = intervals[0][1], 0
        for x in intervals[1:]:
            if x[0] < curr_end:
                cnt += 1
                curr_end = min(curr_end, x[1])
            else:
                curr_end = x[1]
        return cnt


'''
U r so beautiful~~
时隔这么多年又一次发现你的美吖
可爱的配色 清脆的键盘声 如此elegant的结构
人心复杂 很多时候我自己都不懂我自己 可你永远这么理性真实的陪伴在我身边
真好啊 就这样相爱相杀一辈子吧kk
书于2019.7.8 02:42
'''

