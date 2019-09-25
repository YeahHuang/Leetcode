class Solution:
    #你看这个题 你拿到的时候一脸懵比 觉得完全无法下手 可是真的静下心来去做 这个hard的题目19min就AC了 代码也很干净 和 solution几乎无差 要有信心呀
    def minDistance(self, word1: str, word2: str) -> int:
        f = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)): #一开始忘记初始化了 这4行以后要留意吖
            f[i+1][0] = i+1
        for j in range(len(word2)):
            f[0][j+1] = j+1
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    f[i+1][j+1] = f[i][j]
                else:
                    f[i+1][j+1] = min(f[i][j], f[i+1][j], f[i][j+1]) + 1
        return f[-1][-1]

