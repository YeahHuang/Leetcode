class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        
        10:36 - 
        
        最暴力的 对于nums2 哈希 pos[num] = i 
        然后从前往后走 看看 哪个最大
        
        优化： 从后往前 stack
        当前的比它大 直接pop 
        
        从前往后pop
        """
        
        # for i, num in enumerate(nums2):
        #     pos[num] = i
        
        stack = [] #递减的stack
        m = {}
        for i, num in enumerate(nums2):
            #stack为空
            #>栈顶元素 pop到<
            #然后append
            m.setdefault(num, -1)
            while stack and num > stack[-1]:
                num0 = stack.pop()
                m[num0] = num
            stack.append(num)
        return [m[num] for num in nums1]