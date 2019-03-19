class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2): 
        """
        1次AC
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        if n == 0:
            raise ValueError #这个写法学到了

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if (i == 0 or nums1[i-1] <= nums2[j]) and (i == m or nums2[j-1] <= nums1[i]):
                break
            elif i != 0 and nums1[i-1] > nums2[j]:
                imax = i-1
            else:
                imin = i+1

        if i == 0:
            max_of_left = nums2[j-1]
        elif j == 0:
            max_of_left = nums1[i-1]
        else:
            max_of_left = max(nums1[i-1],nums2[j-1])

        if (m+n) % 2 == 1:
            ret = max_of_left
        else:
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            ret = (max_of_left + min_of_right) / 2.0
        '''
        if i == 0:
            max_of_left = nums2[j-1]
            min_of_right = nums1[i]
        elif i == m:
            max_of_left = nums1[i-1]
            min_of_right = nums2[j]
        else:
            max_of_left = max(nums1[i-1],nums2[j-1])
            max_of_right = min(nums1[i], nums2[j])

        if (m+n) % 2 == 1:
            ret = max_of_left
        else:
            ret = (max_of_left + max_of_right) / 2.0
        '''

        return ret

        #RE了超多次 nums1 nums2 弄混 / 把c++的（）？ ：混淆到python / 边界的判断 空数组etc

