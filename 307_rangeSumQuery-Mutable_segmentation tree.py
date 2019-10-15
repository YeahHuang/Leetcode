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
        while i<=j:
            if i%2==1:
                sum += self.seg_tree[i]
                i+=1
            if j%2==0:
                sum +=  self.seg_tree[j]
                j-=1
            i,j = i//2,  j//2
        return sum
#PS 这里尝试了把i//2 换做 i>>1  i%2换做i&1 但最后无差 我想可能是python编译器已经对类似的东西做了该骚操作了


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)