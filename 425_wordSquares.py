class Solution:
    """
    题目： 形成一个每一行/每一列的单词 都在word-dict 里
    e.g. Input:
    ["abat","baba","atan","atal"]

    Output:
    [
      [ "baba",
        "abat",
        "baba",
        "atan"
      ],
      [ "baba",
        "abat",
        "baba",
        "atal"
      ]
    ]
    我本来想着直接暴力枚举 相当于 Cn4 * ...
    可能有点乱了 因为一步步的匹配 可能直接手动写5次模型。
    答案的写法 相当于把题目拆分成我们熟悉的unit板块 dfs + 前缀树  会很模版化 挺好的

    below is directly copied from https://leetcode.com/problems/word-squares/'s solution
    """

    def wordSquares(self, words: List[str]) -> List[List[str]]:

        self.words = words
        self.N = len(words[0])
        self.buildTrie(self.words)

        results = []
        word_squares = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def buildTrie(self, words):
        self.trie = {}

        for wordIndex, word in enumerate(words):
            node = self.trie
            for char in word:
                if char in node:
                    node = node[char]
                else:
                    newNode = {}
                    newNode['#'] = [] #前缀树直接哈希打表 还挺酷的 其实也不会很占空间 可以考虑
                    node[char] = newNode
                    node = newNode
                node['#'].append(wordIndex)

    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return [self.words[wordIndex] for wordIndex in node['#']]