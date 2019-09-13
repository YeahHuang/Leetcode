class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        prev = [[]]
        for i, num in enumerate(nums):
            cur = []
            for j in range(len(prev[-1])+1):
                for tmp_list in prev:
                    cur.append(tmp_list[:j]+[num]+tmp_list[j:])
            prev = cur
        return prev

    #python是有自带库的:
    return list(itertools.permutations(nums))