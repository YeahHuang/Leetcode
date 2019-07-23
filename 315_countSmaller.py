class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        #Sol1 O(n*n)
        '''Sol2 O(nlgn) 在他前面的 排队扔掉 但是非常random 把它小一个的 如果在右侧的话 看看有几个 然后就排除了一部分 
            1. hashmap 可以记录sort后的位置 + 目前的位置 
            2. 一个最近的比它小的元素 一个是最靠近它的比它小的数 找一个最近的比它大的数
            应该是不难的
        '''
        count = [0] * len(nums)
        nums.reverse()
        sorted_nums = []
        for i, num in enumerate(nums):
            l = 0
            r = i-1
            while l<=r:  
                mid = (l+r)//2
                if sorted_nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            count[i] = l 
            sorted_nums.insert(l, num)
        return count.reverse()