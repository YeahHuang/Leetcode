class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #Sol 1      40ms 13.3M   mlgm + nlgn
        nums1, nums2 = sorted(nums1), sorted(nums2)
        q = p1 = p2 = 0
        inter = []
        
        while True:
            try:
                if nums1[p1] > nums2[p2]:
                    p2 += 1
                elif nums1[p1] < nums2[p2]:
                    p1 += 1
                else:
                    inter.append(nums1[p1])
                    p1 += 1 
                    p2 += 1
            except IndexError:
                break

        return inter

        #Sol 2      36ms 13.36ms  nearly m + n
        counts = {} 
        inter = []
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
        for num in nums2:
            if num in counts and counts[num]>0:
                counts[num] -= 1
                inter.append(num)
        return inter


        #Sol 3      68ms 13.40M 虽然不快但是用set的& 真的还挺酷的
        return sum([[i]*min(nums1.count(i),nums2.count(i)) for i in set(nums1)&set(nums2)],[])


        #Sol 4      40ms 13.2M
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        return list((c1&c2).elements())