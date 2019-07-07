#据说Similar to 252 253 435
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def smaller(interval0:List[int], interval1:List[int]):
            return interval0[0]<interval1[0] or (interval0[0]==interval1[0] and interval0[1]<interval1[1])

        if len(intervals)==0:
            return []
        
        ans = []
        debug = False

        #sort

        #Sol 1
        #intervals.sort(key=lambda x: x[0])  44ms
        #关于python的内置list sort！！！ https://github.com/python/cpython/blob/master/Objects/listobject.c  
        #listobject.c  1223行的binary sort. 和 2443行左右的具体stable 倒置流程 仔细看呀。 
        
        # Sol2&3 TLE / 改变移动策略 2464ms
        '''
        for i in range(len(intervals)): #用 n = len(intervals) 替代 只会增加20ms
            tmp_left = intervals[i][0]
            j = i-1
            while j>=0 and tmp_left < intervals[j][0]: #和下面的速度差别不大
            #while j>=0 and smaller(tmp_inter, intervals[j]):
                #intervals[j+1] = intervals[j]
                j -= 1
            intervals.insert(j+1, intervals.pop(i)) #用这个改变移动方式 快很多
            #intervals[j+1] = [tmp_left, tmp_right]
        '''
        
        
        #Sol3 二分插入 96ms
        for i in range(len(intervals)): #用 n = len(intervals) 替代 只会增加20ms
            tmp_left = intervals[i][0]
            l = 0
            r = i-1
            m = (l+r) // 2
            while l<r:
                if debug:
                    print(l,r, m)
                if tmp_left>=intervals[m][0] and tmp_left<=intervals[m+1][0]:
                    break
                elif tmp_left>intervals[m][0]:
                    l = m + 1   #一开始错误的写成了 l = m omg 二分还是不清晰哦
                else:
                    r = m - 1
                m = (l + r) // 2
            
            if debug:
                print(tmp_left, l, r, m)
            if m+1 < len(intervals) and tmp_left>intervals[m+1][0]: #边界条件的判断 一开始错误的写成了>= 
                m += 1
            if debug:
                print(tmp_left,intervals[m][0], l, r, m)
            if m>=0 and tmp_left<intervals[m][0]:   #我觉得还是有些问题emmm
                m -= 1
            
            if debug:
                print("insert %d from %d"%(m+1,i))
            #while j>=0 and tmp_left < intervals[j][0]: #和下面的速度差别不大
            #while j>=0 and smaller(tmp_inter, intervals[j]):
                #intervals[j+1] = intervals[j]
            #    j -= 1
            intervals.insert(m+1, intervals.pop(i)) #用这个改变移动方式 快很多
            if debug:
                print(tmp_left, l,r,m)
                print(intervals)
            #intervals[j+1] = [tmp_left, tmp_right]

        cur_left = intervals[0][0] #一开始打错写成了intervals[0] 双维度数组注意吖
        cur_right = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > cur_right:
                if debug:
                    print(cur_left, cur_right)
                ans.append([cur_left, cur_right]) #一开始错写成了ans.push_back() 那是c++ vector的用法吖 别弄混了
                cur_left = intervals[i][0]
                cur_right = intervals[i][1]
            elif intervals[i][1] > cur_right:
                cur_right = intervals[i][1] #一开始打错写成了intervals[i][0]
        
        ans.append([cur_left, cur_right])
        #if ans[-1][1]!=cur_right: 
            
        #else:
        #    print("Note!")
        #    print(ans)
        return ans

        #下面来看大神的代码！
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key = lambda i: i[0]): #自带的比我的96ms 快到了68ms 有机会一定要细细研究吖
            if out and i[0]<=out[-1][1]:
                out[-1][1] = max(i[1],out[-1][1])
            else:
                out.append(i) #一开始和大神i.start i.end 一样写了 out += i 会报错 list需要append 不然直接替代的
        return out
    

