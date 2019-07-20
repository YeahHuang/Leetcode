class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        #version1 没二分插入 因为觉得已经sort 212ms
        def insert(buildings, l, r, h):
            if not buildings or l >= buildings[-1][0]:
                buildings.append([l,r,h])
            else:
                for i, building in enumerate(buildings):#一开始没有考虑buildings 都已经空了和在最后插入的情况
                    if l <= building[0]:
                        buildings.insert(i, [l, r, h])
                        break

        #Improved version:+了插入 212ms -> 116ms ✌️
        #referenced link :https://jeffreystedfast.blogspot.com/2007/02/binary-insertion-sort.html
        def insert(buildings, l, r, h):
            if not buildings or l >= buildings[-1][0]:
                buildings.append([l,r,h])
            else:
                left = 0
                right = len(buildings) - 1
                mid = (left + right) // 2
                while left < right:                  
                    if l > buildings[mid][0]:
                        left = mid + 1
                    elif l < buildings[mid][0]:
                        right = mid 
                    else:
                        break
                    mid = (left + right) // 2
                buildings.insert(mid, [l,r,h])
            if debug:
                print("new buildings:", buildings)

        if not buildings:
            return []         
        max_l, max_r, max_h = buildings.pop(0)
        ans = [[max_l, max_h]]
        debug = False
        #用heapq来改进这个
        while buildings:
            l, r, h = buildings.pop(0)
            if debug:
                print("l,r,h: ", l, r, h)
                print("max_l, max_r, max_h:", max_l, max_r, max_h)
            if ans and ans[-1][0]==l and ans[-1][1]<h:
                ans.pop()
            if l >= max_r:      #no overlap
                if l > max_r:
                    ans.append([max_r,0])
                if l > max_r or max_h != h:#最初忘记写这个条件了 认为即使等于 新的点一定存在 没有考虑到并列的情况  m
                    ans.append([l, h]) 
                max_l, max_r, max_h = l, r, h
            else:               #has overlap
                if h > max_h:
                    if r >= max_r:
                        ans.append([l,h])
                        max_l, max_r, max_h = l, r, h
                    else:
                        insert(buildings, r, max_r, max_h) #稍后implement
                        ans.append([l,h])
                        max_l, max_r, max_h = l, r, h
                elif h == max_h:
                    max_r = max(max_r, r)
                else:
                    if r <= max_r:
                        continue
                    else:
                        insert(buildings, max_r, r, h)

            if debug:
                print("ans:" , ans)
                
        ans.append([max_r, 0])
        return ans


        #别人用heapq的维护方法 120ms
        def getSkyline(self, buildings):
    events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
    res, hp = [[0, 0]], [(0, float("inf"))]
    for x, negH, R in events:
        while x >= hp[0][1]: 
            heapq.heappop(hp)
        if negH: 
            heapq.heappush(hp, (negH, R))
        if res[-1][1] + hp[0][0]: 
            res += [x, -hp[0][0]],
    return res[1:]

