class Solution:
    #Sol1 从前往后 需要insert 36ms
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Test Cases：
        [] [1,2,3]
        [1,2,3] [4,5,6]
        [1] [2,3,4]   insert(1,2) m = 2 
        """
        p1 = 0
        p2 = 0
        ori_length = len(nums1)
        while p2<n:
            if p1==m:
                nums1[m:(m+n-p2)] = nums2[p2:n]#idx 不能搞错吖
                break
                #一开始错误的写成了 nums1 += nums2[p2:] 
            while p1<m and nums2[p2] > nums1[p1]:
                p1 += 1
            nums1.insert(p1, nums2[p2]) #一开始错误的写成了nums1.insert(p1, p2)
            m += 1
            p2 += 1
        nums1[:] = nums1[:ori_length]

    #Sol2 从后往前 44ms
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        q = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p1>=0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[q] = nums1[p1]
                p1 -= 1
            else:
                nums1[q] = nums2[p2]
                p2 -= 1
            q -= 1
        if p2>=0: #一开始写成了 if p2 导致忽略了=0的时候的情况 WA一次
            nums1[:p2+1] = nums2[:p2+1]
            
