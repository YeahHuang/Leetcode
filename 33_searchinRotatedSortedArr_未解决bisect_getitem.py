class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #Sol1 我的 新问题拆解为2已知小问题 52ms 1-find rotate point 2-search rotate point

        #find rotate point 
        n = len(nums)
        l, r = 0, len(nums)-1 #0 1 2 3 4 5    #5 0 1 2 3 4  #4 5 0 1 2 3
        debug = True
        while l <= r:
            
            if nums[l]<nums[r]:
                print("No need to find! break")
                if r<n-1 and nums[r]>nums[r+1]:
                    mid = r 
                    nums[:] = nums + nums[:mid+1]
                    l, r = mid+1, len(nums)-1
                break
            mid = (l+r)//2
            if debug:
                print(l,r, mid)
            if nums[mid]>nums[mid-1]  and nums[mid]>nums[mid+1]:
                print("already find! mid=%d"%mid)
                nums[:] = nums + nums[:mid+1]
                l, r = mid+1, len(nums)-1
                break
            elif nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        #search lgn 
        while l<=r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l%n if l<len(nums) and nums[l]==target else -1 #因为没有判定l的范围 WA了一次


        '''
        Sol2  + 针对新问题的分析 也是52ms
        nums[l] <=target < nums[r] [l,r]有序 且在其中
                  target > nums[l] > nums[r]
                           nums[l] > nums[r] > target 


        ''' 
        l, r = 0, len(nums) - 1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                l = mid
                break
            elif nums[l]<=target<nums[mid] or target >= nums[l]> nums[mid] or nums[l]>nums[mid]>target: 
                #可以用 if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]): xor代替
                #一开始WA是因为 没有判断nums[l]=target的情况 
                r = mid - 1
            else:
                l = mid + 1
            
        return l if l<len(nums) and nums[l]==target else -1 

        '''可以像大神一样 自定义bisect
        p.s.  根据bisect的官方文档 用lo, hi代替l,r  似乎更加标准
        这里的用法相当于给bisect定义了key 参考https://stackoverflow.com/questions/27672494/how-to-use-bisect-insort-left-with-a-key/37895216
Example：      
class KeyifyList(object):
    def __init__(self, inner, key):
        self.inner = inner
        self.key = key

    def __len__(self):
        return len(self.inner)

    def __getitem__(self, k):
        return self.key(self.inner[k])


if __name__ == '__main__':
    import bisect
    L = [(0, 0), (1, 5), (2, 10), (3, 15), (4, 20)]
    assert bisect.bisect_left(KeyifyList(L, lambda x: x[0]), 3) == 3
    assert bisect.bisect_left(KeyifyList(L, lambda x: x[1]), 3) == 1
        '''
        
    def search(self, nums, target):
        self.__getitem__ = lambda i: \
            (nums[0] <= target) ^ (nums[0] > nums[i]) ^ (target > nums[i])
        i = bisect.bisect_left(self, True, 0, len(nums)) #相当于自己定义比较函数 如上 但第二个为什么是True呢？
        return i if target in nums[i:i+1] else -1

        #Sol3 大神讲更大神的做法 https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple