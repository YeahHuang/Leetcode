class Solution:
    #Sol1 把46的加了个set 64ms beats70%
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        prev = set()
        prev.add(()) #一开始写的是prev.add([]) 后来才知道list不能被map 所以不能是set的元素
        for i, num in enumerate(nums):
            cur = set()
            for j in range(i+1):
                for tmp_tuple in prev: #list和tuple的转换学到了
                    tmp_list = list(tmp_tuple)
                    cur.add(tuple(tmp_list[:j]+[num]+tmp_list[j:]))
            prev = cur
        return list(prev)

    #Sol2 把46的增加了一个 新添加元素的时候 只在原list当前num前加 56ms beats 97% referenced from #cbmbbz
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        prev = [[]]
        for i, num in enumerate(nums):
            cur = []
            for tmp_list in prev:
                for j in range(i+1):
                    cur.append(tmp_list[:j]+[num]+tmp_list[j:])
                    if j < i and tmp_list[j]==num: #trick的核心！！！
                        break
            prev = cur
        return prev
