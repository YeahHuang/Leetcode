class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        #Sol1 这2行都是都是112ms
        return [i for i, times in cnt.most_common(k)] 
        #Sol2
        return heapq.nlargest(k, cnt.keys(), key=cnt.get)
        #Sol3 用zip来代替前面的i循环 但是反而要120ms
        return list(zip(*collections.Counter(nums).most_common(k)))[0] 
        
        '''
        *: most_common() returns a list of the n most common elements and their counts and ' * ' unzips the list of tuples returned by most_common().
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print(collections.Counter(nums).most_common(k))
        print(*collections.Counter(nums).most_common(k))
        print(zip(*collections.Counter(nums).most_common(k)))
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
        这4个的输出分别是：
        [(1, 3), (2, 2)]
        (1, 3) (2, 2)
        <zip object at 0x7f44d426fb08>
        '''