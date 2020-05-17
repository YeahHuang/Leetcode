#referenced from diverseSubarray_hit_tom.py RMQ template
#c++ 可以见同名的
#RSQ 可以参考 https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
import collections

global ma, lazy,b

def pushdown(i):
    global ma, lazy
    if lazy[i]:
        ma[i<<1] += lazy[i]
        ma[i<<1 | 1] += lazy[i]
        lazy[i<<1] += lazy[i]
        lazy[i<<1 | 1] += lazy[i]
        lazy[i] = 0

def pushup(i):
    global ma
    ma[i] = max(ma[i<<1] , ma[i<<1|1])

def build(i, l, r):
    global lazy, ma, b
    lazy[i] = 0
    if l == r:
        ma[i] = b[l]
    else:
        mid = l+r >> 1
        build(i<<1, l, mid)
        build(i<<1|1, mid+1, r)
        pushup(i)

def update(i, l, r, x, y, value):
    global ma, lazy
    if x<=l<=r<=y:
        ma[i] += value
        lazy[i] += value
    else:
        pushdown(i)
        mid = l+r >> 1
        if x<=mid: 
            update(i<<1, l, mid, x, y, value)
        if mid<y:
            update(i<<1|1, mid+1, r, x, y, value)
        pushup(i)

def query(i, l, r, x, y):
    if x<=l<=r<=y:
        res = ma[i]
    else:
        res = 0
        pushdown(i)
        mid = l+r>>1
        if x<=mid:
            res = query(i<<1, l, mid, x, y)
        if mid < y:
            res = max(res, query(i<<1|1, mid+1, r,x, y))
    return res



#copied from diverseSubarray_large.py

def insert(x, l, r, i, j, value):
    global seg
    if l==i and r == j:
        seg[x] = seg[x]._replace(mark=seg[x].mark + value)
        return
    mid = (l+r)//2
    if j<=mid:
        insert(x*2, l, mid, i, j, value)
    elif i>mid:
        insert(x*2+1, mid+1, r, i, j, value)
    else:
        insert(x*2, l, mid, i, mid, value)
        insert(x*2+1, mid+1, r, mid+1, j, value)
    seg[x] = seg[x]._replace(value = max(seg[x*2].value+seg[x*2].mark, seg[x*2+1].value, seg[x*2+1].mark))

T = int(input())
Seg = collections.namedtuple('Seg',['value','mark'])


ans = max(ans, seg[1].value + seg[1].mark)


#copied from 307_rangeSumQuery-Mutable 和RMQ一样 RSQ(range sum query) 同样是segmentTree的常见操作 
#https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.seg_tree = [0]*self.n + nums
        for i in range(self.n-1, 0, -1):
            self.seg_tree[i] = self.seg_tree[i*2] + self.seg_tree[i*2+1]
        #print(self.seg_tree)
        
    def update(self, i: int, val: int) -> None:
        i += self.n
        self.seg_tree[i] = val
        while i>0:
            if i%2==1: #一开始这里写反了 WA
                self.seg_tree[i//2] = self.seg_tree[i] + self.seg_tree[i-1]
            else:
                self.seg_tree[i//2] = self.seg_tree[i] + self.seg_tree[i+1]
            i=i//2
        
        
    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        i, j = i+self.n, j+self.n #一开始忘记加 WA
        while i<=j: #可能这里就是一个求LCA(lowest common ancester)的过程
            if i%2==1:
                sum += self.seg_tree[i]
                i+=1
            if j%2==0:
                sum +=  self.seg_tree[j]
                j-=1
            i,j = i//2,  j//2


#https://leetcode.com/problems/my-calendar-iii/discuss/214831/Python-13-Lines-Segment-Tree-with-Lazy-Propagation-O(1)-time
#Leetcode 732
class MyCalendarThree(object):

    def __init__(self):
        self.seg = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)
        
    def book(self, start, end):
        def update(s, e, l = 0, r = 10**9, ID = 1):
            if r <= s or e <= l: return 
            if s <= l < r <= e:
                self.seg[ID] += 1
                self.lazy[ID] += 1
            else:
                m = (l + r) // 2
                update(s, e, l, m, 2 * ID)
                update(s, e, m, r, 2*ID+1)
                self.seg[ID] = self.lazy[ID] + max(self.seg[2*ID], self.seg[2*ID+1])
        update(start, end)
        return self.seg[1] + self.lazy[1]
